# Copyright (c) 2015 David Wilson
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

from Interactors.GameInteractors import GetGamesInteractor
from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGamesInteractor(InteractorTestBase):
    """Unit tests for the GetGamesInteractor class""" 

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = GetGamesInteractor()
        self.__target.persistence = self.persistence
        self.__execute = self.__target.execute(self.__get_params())

    def test_is_instance_of_interactor(self):
        """Tes tthat GetGamesInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_calls_persistence_method(self):
        """Test that calling GetGamesInteractor.execute causes persistence.get_all_games to be called"""
        self.__execute()
        self.persistence.get_all_games.assert_was_called_with(self.__get_params())

    def test_with_platform_calls_get_all_games_for_platform_persistence_method(self):
        """Test that calling GetGamesInteractor.execute causes persistence.get_all_games_for_platform to be called"""
        self.__execute()
        self.__target.persistence.get_all_games_for_platform.assert_was_called_with(self.__get_params())
        
    def test_user_id_not_set_gives_value_error(self):
        """Test that calling GetGamesInteractor.execute with null user_id causes ValueError to be raised"""
        p = self.__get_params()
        p.user_id = None
        self.assertRaises(ValueError, self.__target.execute, p)

    def __get_params(self):
        p = GetGamesInteractorParams()        
        p.number_of_games = 10
        p.sort_field = None
        p.sort_direction = "asc"
        p.platform = "platform"
        p.user_id = "1234"
        return p
        
