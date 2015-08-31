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

import Interactors.PlatformInteractors as pi
import Interactors.Interactor as i
import Platform as p
import Tests.Interactors.InteractorTestBase as itb


class TestDeletePlatformInteractor(itb.InteractorTestBase):
    """Unit tests for DeletePlatformInteractor"""

    def setUp(self):
        """setUp function for all unit tests in this class."""
        super().setUp()

        def get_platforms():
            platform = {'id': 'id',
                        'name': 'a platform'}
            return [p.Platform.from_dict(platform)]

        self.__target = pi.DeletePlatformInteractor()
        self.persistence.get_platforms = Mock(side_effect=get_platforms)
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field

    def test_is_instance_of_interactor(self):
        """Test that DeletePlatformInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, i.Interactor)

    def test_execute_calls_delete_platform_persistence_method(self):
        """Test that calling DeletePlatformInteractor.execute causes persistence.delete_platform to be called"""
        platform = p.Platform()
        platform.id = "id"
        self.__target.execute(platform=platform.id)
        self.persistence.delete_platform.assert_called_with(platform.id)

    def test_execute_with_none_platform_raises_type_error(self):
        """Test that calling DeletePlatformInteractor.execute with a null platform causes TypeError to be raised"""
        self.assertRaises(TypeError, self.__target.execute, None)
        
    def test_execute_platform_does_not_exist_raises_platform_not_found_exception(self):
        """Test that when the platform to be deleted does not exist, PlatformNotFoundException is raised"""
        platform = p.Platform()
        platform.id = 'non-existant'
        self.assertRaises(pi.PlatformNotFoundException, self.__target.execute, platform.id)
