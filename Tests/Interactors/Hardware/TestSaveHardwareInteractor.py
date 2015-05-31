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
from Interactors.HardwareInteractors import SaveHardwareInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestSaveHardwareInteractor(InteractorTestBase):
    """Unit tests for the SaveHardwareInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = SaveHardwareInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field
        self.__hardware = self.get_hardware(name="name", platform="platform", num_owned=1, num_boxed=1)

    def test_is_instance_of_interactor(self):
        """Assert that SaveHardwareInteractor is an instance of Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        """Test that calling SaveHardwareInteractor.execute causes persistence.save_hardware to be called"""
        hardware = self.get_hardware()
        user_id = "1234"
        self.__execute(hardware, user_id)
        self.persistence.save_hardware.assert_called_with(hardware, user_id)

    def test_execute_with_null_hardware_raises_type_error(self):
        """Test that calling SaveHardwareInteractor.execute with a null hardware parameter causes a TypeError to be 
        raised"""
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_with_id_set_raises_value_error(self):
        """Test that calling SaveHardwareInteractor.execute with hardware.id set causes a ValueError to be raised"""
        self.assertRaises(ValueError, self.__execute, self.get_hardware(hardware_id="id"))

    def test_execute_validates_string_fields(self):
        """Test that calling SaveHardwareInteractor.execute causes the string members of Hardware to be validated"""
        fields = {"Hardware name": self.__hardware.name,
                  "Platform": self.__hardware.platform} 
    
        self.__assert_field_validation_called(fields, self.validate_string_field_was_called_with)

    def test_execute_validates_integer_fields(self):
        """Test that calling SaveHardwareInteractor.execute causes the integer members of Hardware to be validated"""
        fields = {"Number owned": self.__hardware.num_owned,
                  "Number boxed": self.__hardware.num_boxed}

        self.__assert_field_validation_called(fields, self.validate_integer_field_was_called_with)

    def __assert_field_validation_called(self, fields, called_with_func):
        self.__execute(self.__hardware)
        
        for f in fields:
            self.assertTrue(called_with_func(f, fields[f]), f)

    def __execute(self, args, user_id="userid"):
        self.__target.execute(args, user_id)
