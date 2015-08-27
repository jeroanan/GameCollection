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

from unittest.mock import Mock

import Interactors.PlatformInteractors as pi
from Interactors.Interactor import Interactor
import Platform as p
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestAddPlatformInteractor(InteractorTestBase):
    """Unit tests for the AddPlatformInteractor class"""

    def setUp(self):
        """setup function for all unit tests in this class"""

        def get_stored_platforms():
            existing_platforms = [{
                "name": "existing_platform",
                "description": "It exists"
            }, {
                "name": "another one",
                "description": "This also exists"
            }]

            platforms = []
            for ep in existing_platforms:
                platforms.append(p.Platform.from_dict(ep))
            
            return platforms

        super().setUp()
        self.__target = pi.AddPlatformInteractor()
        self.__target.persistence = self.persistence
        self.__target.persistence.get_platforms = Mock(return_value=get_stored_platforms())
        self.__target.validate_string_field = self.validate_string_field
        self.__target.validate_integer_field = self.validate_integer_field

    def test_is_interactor(self):
        """Test that AddPlatformInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_platform_raises_type_error(self):
        """Test that calling AddPlatformInteractor.execute with a null platform causes TypeError to be raised"""
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_non_blank_id_raises_value_error(self):
        """Test that calling AddPlatformInteractor.execute with a populated platform id causes ValueError to be raised"""
        self.assertRaises(ValueError, self.__target.execute, self.get_platform(platform_id="id"))

    def test_execute_validates_platform_name_field(self):
        """Test that calling AddPlatformInteractor.execute causes the platform's name to be validated"""
        platform = self.get_platform(name="")
        self.__target.execute(platform)
        self.assertTrue(self.validate_string_field_was_called_with("Platform name", platform.name))

    def test_execute_calls_persistence_to_add_platform(self):
        """Test that calling AddPlatformInteractor.execute causes persistence.add_platform to be executed"""
        self.__target.execute(self.get_platform(name="platform"))
        self.assertTrue(self.persistence.add_platform.called)

    def test_execute_calls_persistence_to_get_all_platforms(self):
        """
        Test that calling AddPlatformInteractor.execute causes persistence.get_platforms to be executed.
        This will then be used to check whether the name of the platform we're trying to add already exists.       
        """
        self.__target.execute(self.get_platform(name="platform"))
        self.assertTrue(self.persistence.get_platforms.called)

    def test_execute_with_existing_platform_name_raises_platform_exists_exception(self):
        self.assertRaises(pi.PlatformExistsException, self.__target.execute, self.get_platform(name='existing_platform'))
