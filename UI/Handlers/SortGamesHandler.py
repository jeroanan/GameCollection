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


class SortGamesHandler(AuthenticatedHandler):
    """Handle requests to sort the user's games collection"""

    def get_page(self, args):
        """Handle requests to sort the user's games collection.
        :param args: A dictionary containing the following keys:
                    * field (default: title)
                    * sortdir (default: <empty string>)
                    * numrows (default: 0)
        :returns: A rendered HTML page containing the sorted games collection"""
        super().get_page(args)
        interactor = self.interactor_factory.create("GetGamesInteractor")
        sort_field = args.get("field", "title")
        sort_direction = args.get("sortdir", "")
        number_of_games = int(args.get("numrows", 0))

        p = GetGamesInteractorParams.from_dict({
            "sort_field": sort_field,
            "sort_direction": sort_direction,
            "number_of_games": number_of_games,
            "user_id": self.session.get_value("user_id")})

        games = interactor.execute(p)
        return self.renderer.render("games.html", games=games, game_sort_field=sort_field, game_sort_dir=sort_direction)
