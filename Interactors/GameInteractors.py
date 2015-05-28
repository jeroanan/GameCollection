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

from Interactors.Interactor import Interactor


class AddGameInteractor(Interactor):

    def execute(self, game, user_id):
        self.__validate(game)
        self.persistence.add_game(game, user_id)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.__validate_game_id(game)
        self.validate_string_field("Game title", game.title)
        self.validate_string_field("Platform", game.platform)
        self.validate_integer_field("Number of copies", game.num_copies)
        self.validate_integer_field("Number of boxed items", game.num_boxed)
        self.validate_integer_field("Number of manuals", game.num_manuals)

    def __validate_game_id(self, game):
        if len(game.id) > 0:
            raise ValueError("Game id must be empty when adding a new game")

