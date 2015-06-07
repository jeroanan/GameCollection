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


class SaveGameHandler(AuthenticatedHandler):
    """Handle requests to save a game"""

    def get_page(self, params):
        """Handles requests to save a game
        :param params: A dictionary. For details on what keys the dictionary should contain, see
        Game.from_dict()."""
        super().get_page(params)
        
        if not self.validate_params(params, ["title", "platform"]):
            return ""
        interactor = self.interactor_factory.create("AddGameInteractor")
        interactor.execute(game=Game.from_dict(params), user_id=self.session.get_value("user_id"))
