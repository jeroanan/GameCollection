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

import Game as g
import Persistence.Exceptions.GameNotFoundException as gnfe
import UI.Handlers.AuthenticatedHandler as ah


class EditGameHandler(ah.AuthenticatedHandler):
    """Handles requests for the Edit Game page"""
    
    def get_page(self, args):
        """The Edit game page
        :param args: A dictionary containing a key "gameid" whose value is the uuid of a game
        :returns: An rendered edit page. If the page isn't found or the current user can't
        access the game then a "Game Not Found" message will display.
        """
        super().get_page(args)

        interactor_get = lambda x: self.interactor_factory.create(x).execute()
        platforms =  interactor_get("GetPlatformsInteractor")
        genres = interactor_get("GetGenresInteractor")

        def get_game(game_id):
            get_game_interactor = self.interactor_factory.create("GetGameInteractor")
            return get_game_interactor.execute(game_id=game_id, user_id=self.session.get_value("user_id"))

        game_found = True
        game = g.Game()
        try:            
            game = get_game(args.get("gameid", ""))            
            page_title = "{title} ({platform})".format(title=game.title, platform=game.platform)
        except gnfe.GameNotFoundException:
            game_found = False
            page_title = "Game Not Found"

        return self.renderer.render("editgame.html", game=game, title=page_title, 
                                    platforms=platforms, game_found=game_found, 
                                    genres=genres)

    

    
