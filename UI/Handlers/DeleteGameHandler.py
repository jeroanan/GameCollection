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

from Game import Game
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class DeleteGameHandler(AuthenticatedHandler):
    """Handles Game deletion requests"""

    def __init__(self, interactor_factory, renderer):
        """Initialise an instance of DeleteGameHandler.
        :param interactor_factory: The factory object to use for constructing interactors
        :param renderer: The object to use to render output html
        """
        super().__init__(interactor_factory, renderer)
        self.__get_game = lambda args: Game.from_dict({"id": args.get("id", "")})
    
    def get_page(self, args):
        """Handles Game deletion requests.
        This is really intended to be used as an ajax request rather than a webpage, so
        it doesn't give much in the way of user feedback. If the user is not currently logged
        in then it will redirect to the homepage.
        :param args: A dictionary containing the key "gameid". gameid contains the uuid of the game to be deleted.
        :returns: If gameid is not present in args then an empty string is returned. Else None is returned.
        """
        super().get_page(args)
        if not self.validate_params(args, ["id"]):
            return ""
        self.__execute_interactor(self.__get_game(args))

    def __execute_interactor(self, game):
        interactor = self.interactor_factory.create("DeleteGameInteractor")
        interactor.execute(game, self.session.get_value("user_id"))
