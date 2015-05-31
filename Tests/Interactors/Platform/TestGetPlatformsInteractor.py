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

from Interactors.PlatformInteractors import GetPlatformsInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetPlatformsInteractor(InteractorTestBase):
    """Unit tests for the GetPlatformsInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = GetPlatformsInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        """Test that GetPlatformsInteractor is an instance of Interactor"""
        self.__target = GetPlatformsInteractor()
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        """Test that calling GetPlatformsInteractor.execute causes persistence.get_platforms to be called"""
        self.__target.execute()
        self.assertTrue(self.persistence.get_platforms.called)
