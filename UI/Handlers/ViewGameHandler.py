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
import UI.Handlers.AuthenticatedHandler as ah


class ViewGameHandler(ah.AuthenticatedHandler):
    """Handles requests for the View Game page"""

    def get_page(self, params):
        """Handles requests for the View Game page
        :param params: A dictionary containing the following keys:
                       * id - the unique id of the game to be viewed
        :returns: The rendered HTML of the View Game page.
        """
        super().get_page(params)        
        interactor = self.interactor_factory.create("GetGameInteractor")
        game = interactor.execute(g.Game.from_dict(params).id, self.session.get_value("user_id"))
        return self.renderer.render("viewgame.html", title=game.title, game=game)
