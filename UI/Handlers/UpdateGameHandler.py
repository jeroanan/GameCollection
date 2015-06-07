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
from Interactors.Exceptions.PersistenceException import PersistenceException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UpdateGameHandler(AuthenticatedHandler):

    
    def get_page(self, params):
        """Handles Game Update requests.
        This is really intended to be used as an ajax request rather than a webpage, so
        it doesn't give much in the way of user feedback. If the user is not currently logged
        in then it will redirect to the homepage.
        :param params: A dictionary representation of a game object. For details on the keys it can contain,
                      see Game.from_dict().
        :returns: If one of the mandatory entries in params is missing or there is a problem saving then an empty
        string. Else return None.
        """
        super().get_page(params)
        if not self.validate_params(params, ["title", "platform"]):
            return ""        
        if not self.__execute_interactor(params):
            return ""           

    def __execute_interactor(self, params):
        try:
            interactor = self.interactor_factory.create("UpdateGameInteractor")
            game = Game.from_dict(params)
            interactor.execute(game=game, user_id=self.session.get_value("user_id"))
            return True
        except PersistenceException:
            return False
