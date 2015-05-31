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

from Interactors.PlatformInteractors import DeletePlatformInteractor
from Interactors.Interactor import Interactor
from Platform import Platform
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestDeletePlatformInteractor(InteractorTestBase):
    """Unit tests for DeletePlatformInteractor"""

    def setUp(self):
        """setUp function for all unit tests in this class."""
        super().setUp()
        self.__target = DeletePlatformInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field

    def test_is_instance_of_interactor(self):
        """Test that DeletePlatformInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that calling DeletePlatformInteractor.execute causes persistence.delete_platform to be called"""
        platform = Platform()
        platform.id = "id"
        self.__target.execute(platform=platform)
        self.persistence.delete_platform.assert_called_with(platform)

    def test_execute_with_none_platform_raises_type_error(self):
        """Test that calling DeletePlatformInteractor.execute with a null platform causes TypeError to be raised"""
        self.assertRaises(TypeError, self.__target.execute, None)

