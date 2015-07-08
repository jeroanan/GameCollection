# Copyright (c) David Wilson 2015
# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

import Interactors.Game.Params.GetGamesInteractorParams as ggip
import Interactors.Hardware.Params.GetHardwareListInteractorParams as ghlip
import Persistence.Exceptions.UnrecognisedFieldNameException as ufen
import  UI.Handlers.AuthenticatedHandler as ah


class IndexHandler(ah.AuthenticatedHandler):
    """Handles requests for the index page"""

    def __init__(self, interactor_factory, renderer, config):
        """Constructor
        param interactor_factory: An instance of InteractorFactory
        param renderer: An instance of TemplateRenderer
        param config: An instance of Data.Config
        """
        super().__init__(interactor_factory, renderer)

        def count_items(interactor_type_string):
            interactor = self.interactor_factory.create(interactor_type_string)
            return interactor.execute(self.session.get_value("user_id"))        

        self.__count_games = lambda: count_items("CountGamesInteractor")
        self.__count_hardware = lambda: count_items("CountHardwareInteractor")
        self.__config = config
        self.__game_sort = None
        self.__game_sort_dir = None
        self.__hardware_sort = None
        self.__hardware_sort_dir = None

    def get_page(self, args):
        """The index page.
        Currently the index page displays a summary of the user's games and hardware.
        It also displays a games count.
        param args: A dictionary that is comprised of the following keys:
          + gamesort -- The name of the column to sort the list of games by.
          + gamesortdir -- The direction the games should be sorted in.
          + hardwaresort -- The name of the column to sort the list of hardware by.
          + hardwaresortdir -- The direction that the hardware should be sorted in.
        returns: The rendered index page.
                 If one of the sort fields is not recognised then redirect to self without
                 querystring.
        """
        self.check_session()
        self.redirect_if_not_logged_in()

        self.__init_sorting(args)

        try:
            games = self.__get_games()
            hardware = self.__get_hardware()
        except ufen.UnrecognisedFieldNameException:
            raise cherrypy.HTTPRedirect("/")

        return self.renderer.render("index.html", games=games, hardware=hardware,
                                    title="Games Collection", game_sort_field=self.__game_sort,
                                    game_sort_dir=self.__game_sort_dir, hw_sort_field=self.__hardware_sort,
                                    number_of_games=(self.__count_games()),
                                    number_of_hardware=(self.__count_hardware()), hw_sort_dir=self.__hardware_sort_dir)

    def __init_sorting(self, args):

        def init_game_sorting():
            default_sort_field = "title"
            default_sort_direction = "asc"
            self.__game_sort = self.set_if_null(args.get("gamesort", default_sort_field), default_sort_field)
            self.__game_sort_dir = self.set_if_null(args.get("gamesortdir", default_sort_direction),
                                                    default_sort_direction)

        def init_hardware_sorting():

            def if_null(arg_name, default_value):
                return self.set_if_null(args.get(arg_name, default_value), default_value)

            default_sort_field = "name"
            default_sort_direction = "asc"

            self.__hardware_sort = if_null("hardwaresort", default_sort_field)
            self. __hardware_sort_dir = if_null("hardwaresortdir", default_sort_direction)

        init_game_sorting()
        init_hardware_sorting()

    def __get_games(self):
        get_games_interactor = self.interactor_factory.create("GetGamesInteractor")

        p = ggip.GetGamesInteractorParams.from_dict({
                "number_of_games": self.__config.get("front-page-games"""),
                "sort_field": self.__game_sort,
                "sort_direction": self.__game_sort_dir,
                "user_id": self.session.get_value("user_id")})

        try:
            games = get_games_interactor.execute(p)
        except UnrecognisedFieldNameException:
            raise cherrypy.HTTPRedirect("/")
        return games

    def __get_hardware(self):
        p = ghlip.GetHardwareListInteractorParams.from_dict({
            "sort_field": self.__hardware_sort,
            "sort_direction": self.__hardware_sort_dir,
            "user_id": self.session.get_value("user_id"),
            "number_of_items": self.__config.get("front-page-hardware")})

        get_hardware_list_interactor = self.interactor_factory.create("GetHardwareListInteractor")
        return get_hardware_list_interactor.execute(p)

