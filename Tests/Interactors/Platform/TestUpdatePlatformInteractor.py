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

from unittest.mock import Mock

import Interactors.Interactor as i
import Interactors.PlatformInteractors as pi
import Platform as p
import Tests.Interactors.InteractorTestBase as itb


class TestUpdatePlatformInteractor(itb.InteractorTestBase):
    """Unit tests for the UpdatePlatformInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()

        def get_stored_platforms():
            existing_platforms = [{
                "id": "1414",
                "name": "existing_platform",
                "description": "It exists"
            }, {
                "id": "1415",
                "name": "another one",
                "description": "This also exists"
            }]

            platforms = []
            for ep in existing_platforms:
                platforms.append(p.Platform.from_dict(ep))
            
            return platforms

        self.__target = pi.UpdatePlatformInteractor()
        self.__target.persistence = self.persistence
        self.__target.persistence.get_platforms = Mock(return_value=get_stored_platforms())
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field
        self.__platform = self.get_platform()
        self.__platform.id = "1414"

    def test_is_instance_of_interactor(self):
        """Test that UpdatePlatformInteractor is an instance of Interactor"""
        self.assertIsInstance(self.__target, i.Interactor)

    def test_execute_calls_persistence_update_platform(self):
        """Test that calling UpdatePlatformInteractor.execute causes persistence.update_platform to be called"""
        self.__target.execute(self.__platform)
        self.persistence.update_platform.assert_called_with(self.__platform)

    def test_execute_with_none_platform_raises_type_error(self):
        """Test that calling UpdatePlatformInteractor.execute with a null platform causes a TypeError to be raised"""
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_name_field(self):
        """Test that calling UpdatePlatformInteractor.execute causes platform.name to be validated"""
        self.__target.execute(self.__platform)
        self.validate_string_field_was_called_with("Platform name", self.__platform.name)

    def test_execute_for_existing_platform_raises_platform_exists_exception(self):
        """Test that if a platform with the same name already exists (as a different record) then
        PlatformExistsException is raised"""
        self.__platform.name = 'existing_platform'
        self.__platform.id = '1415'
        self.assertRaises(pi.PlatformExistsException, self.__target.execute, self.__platform)
        
    def test_execue_for_non_existing_platform_raises_platform_not_found_exception(self):
        self.__platform.name = 'the hell is this'
        self.__platform.id = '1337'
        self.assertRaises(pi.PlatformNotFoundException, self.__target.execute, self.__platform)
