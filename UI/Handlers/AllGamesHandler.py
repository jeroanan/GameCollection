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

from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AllGamesHandler(AuthenticatedHandler):
    """Handles requests to retrieve all games for a user's collection"""

    def get_page(self, params):
        """Handles requests to retrieve all games for a user's collection
        :param params: A dictionary containing the following keys:
                          * gamesort
                          * gamesortdir
                          * platform
                          * user_id
        :returns: All games in a user's collection for the given platform. If platform is not set then all games in 
                  the user's collection are returned.
        """
        super().get_page(params)
        sort_field = self.set_if_null(params.get("gamesort", "title"), "title")
        sort_direction = self.set_if_null(params.get("gamesortdir", "asc"), "asc")
        platform = params.get("platform", "")
        
        p = GetGamesInteractorParams()
        p.sort_field = sort_field
        p.sort_direction = sort_direction
        p.platform = platform
        p.user_id = self.session.get_value("user_id")
        
        games = list(self.__get_games(p))
        
        return self.renderer.render("allgames.html", games=games, title="All Games", game_sort_field=sort_field,
                                    game_sort_dir=sort_direction, platform=platform,
                                    query="platform=%s" % platform)
        
    def __get_games(self, params):
        interactor = self.interactor_factory.create("GetGamesInteractor")
        return interactor.execute(params)
            
