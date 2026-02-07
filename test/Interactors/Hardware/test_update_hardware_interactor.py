"""Unit tests for UpdateHardwareInteractor."""

from test.Interactors.interactor_test_base import InteractorTestBase
from Interactors.interactor import Interactor
from Interactors.hardware_interactors import UpdateHardwareInteractor


class TestUpdateHardwareInteractor(InteractorTestBase):
    """Unit tests for UpdateHardwareInteractor."""

    def setUp(self):
        super().setUp()
        self.__target = UpdateHardwareInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field
        self.__hardware = self.get_hardware(name="name")

    def test_is_instance_of_interactor(self):
        """Test that UpdateHardwareInteractor is an Interactor."""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that execute calls the persistence method to update hardware."""
        self.__execute(hardware=self.__hardware, user_id="user_id")
        self.persistence.update_hardware.assert_called_with(self.__hardware, "user_id")

    def test_execute_with_none_hardware_raises_type_error(self):
        """Test that execute with None hardware raises TypeError."""
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_validates_name_field(self):
        """Test that execute validates the hardware name field."""
        self.__execute(self.__hardware)
        self.validate_string_field_was_called_with("hardware name", self.__hardware.name)

    def test_execute_validates_platform_field(self):
        """Test that execute validates the hardware platform field."""
        self.__execute(self.__hardware)
        self.validate_string_field_was_called_with("platform", self.__hardware.platform)

    def test_execute_validates_numowned_field(self):
        """Test that execute validates the hardware num_owned field."""
        self.__execute(self.__hardware)
        self.validate_integer_field_was_called_with("Number owned", self.__hardware.num_owned)

    def test_execute_validates_numboxed_field(self):
        """Test that execute validates the hardware num_boxed field."""
        self.__execute(self.__hardware)
        self.validate_integer_field_was_called_with("Number boxed", self.__hardware.num_boxed)

    def __execute(self, hardware, user_id="userid"):
        self.__target.execute(hardware, user_id)
