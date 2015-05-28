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

from Interactors.Exceptions.PersistenceException import PersistenceException
from Interactors.Interactor import Interactor


class AddGameInteractor(Interactor):
    """Add a game"""

    def execute(self, game, user_id):
        """Add a game
        :param game: An object of type Game. The game to be added.
        """
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


class CountGamesInteractor(Interactor):
    """Count the number of games in the user's collection"""

    def execute(self, user_id):
        """Gets the count of games in the user's collection from persistence
        param user_id: The uuid of the user
        returns: The number of games in the user's collection
        """
        return self.persistence.count_games(user_id)

class DeleteGameInteractor(Interactor):
    """Delete a game."""
    
    def execute(self, game, user_id):
        """Tell persistence to delete the given game.
        :param game_id: An object of type Game -- the game to be deleted
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        self.__validate(game)
        self.persistence.delete_game(game, user_id)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.validate_string_field("Game id", game.id)


class GetGameInteractor(Interactor):
    """Get a game"""

    def execute(self, game_id, user_id):
        """Gets a specific game from persistence
        :param game_id: The uuid of the game to be retrieved
        :param user_id: The uuid of the current user
        :returns: A game from persistence
        """
        self.validate_string_field("game id", game_id)
        return self.persistence.get_game(game_id, user_id)


class GetGamesInteractor(Interactor):
    """Get all games in the user's collection"""
    
    def execute(self, params):
        """Gets a list of games in the user's collection from persistence. If a platform is specified then get games for
        that platform, else get games for all platforms.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """
        self.validate_string_field("User Id", params.user_id)
        if params.platform == "" or params.platform is None:
            return self.persistence.get_all_games(params)

        return self.persistence.get_all_games_for_platform(params)


class UpdateGameInteractor(Interactor):
    """Update the details of a game"""
    
    def execute(self, game, user_id):
        """Tells persistence to update a game
        :param game: An object of type Game
        :param user_id: The uuid of the current user
        :returns: None
        """
        self.__validate(game)
        try:
            self.persistence.update_game(game, user_id)
        except:
            raise PersistenceException

    def __validate(self, game):
        if game is None:

            raise TypeError("game")
        self.validate_string_field("Game title", game.title)
        self.validate_string_field("Game platform", game.platform)
        self.validate_integer_field("Number of copies", game.num_copies)
        self.validate_integer_field("Number boxed", game.num_boxed)
        self.validate_integer_field("Number of manuals", game.num_manuals)
