"""Unit tests for the GetGamesInteractor class""" 
# Copyright (c) 2015, 2026 David Wilson
# This file is part of Icarus.

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

from test.Interactors.interactor_test_base import InteractorTestBase
from interactors.game_interactors import GetGamesInteractor
from interactors.game.Params.get_games_interactor_params import GetGamesInteractorParams
from interactors.interactor import Interactor

class TestGetGamesInteractor(InteractorTestBase):
    """Unit tests for the GetGamesInteractor class""" 

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = GetGamesInteractor()
        self.__target.persistence = self.persistence
        self.__execute = self.__target.execute

    def test_is_instance_of_interactor(self):
        """Test that GetGamesInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_wihtout_platform_call_get_all_games_persistence_method(self):
        """Test that calling GetGamesInteractor.execute causes persistence.get_all_games to be 
        called"""
        p = self.__get_params()
        p.platform = ""
        self.__execute(p)
        self.persistence.get_all_games.assert_called_with(p)

    def test_with_platform_calls_get_all_games_for_platform_persistence_method(self):
        """Test that calling GetGamesInteractor.execute causes 
        persistence.get_all_games_for_platform to be called"""
        p = self.__get_params()
        self.__execute(p)
        self.persistence.get_all_games_for_platform.assert_called_with(p)

    def test_user_id_not_set_gives_value_error(self):
        """Test that calling GetGamesInteractor.execute with null user_id causes ValueError to be 
        raised"""
        p = self.__get_params()
        p.user_id = None
        self.assertRaises(ValueError, self.__target.execute, p)

    def __get_params(self):
        return GetGamesInteractorParams.from_dict({
            "number_of_games": 10,
            "sort_field": None,
            "sort_direction": "asc",
            "platform": "p",
            "user_id": "1234"})
