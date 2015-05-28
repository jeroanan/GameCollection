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
    """Add a game"""

    def execute(self, game, user_id):
        """Add a game
        :param game: An object of type game. The game to be added.
        :param user_id: A string. The id of the user the game is to be added for
        """
        self.__validate(game)
        self.persistence.add_game(game, user_id)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.__validate_game_id(game)
        self.__validate_required_string_fields(game)
        self.__validate_required_integer_fields(game)

    def __validate_required_string_fields(self, game):
        validations = {"Game title": game.title,
                       "Platform": game.platform}
        self.validate_string_fields(v, validations[v])

    def __validate_required_integer_fields(self, game):
        validations = {"Number of copies": game.num_copies,
                       "Number of boxed items": game.num_boxed,
                       "Number of manuals": game.num_manuals}
        self.__validate_integer_fields(validations)


    def __validate_game_id(self, game):
        if len(game.id) > 0:
            raise ValueError("Game id must be empty when adding a new game")
