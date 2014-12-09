from Interactors.Interactor import Interactor
from Interactors.UpdateHardwareInteractor import UpdateHardwareInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestUpdateHardwareInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = UpdateHardwareInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field
        self.__hardware = self.get_hardware(name="name")

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute(hardware=self.__hardware)
        self.persistence.update_hardware.assert_called_with(self.__hardware)

    def test_execute_with_none_hardware_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_name_field(self):
        self.__target.execute(self.__hardware)
        self.validate_string_field_was_called_with("hardware name", self.__hardware.name)

    def test_execute_validates_platform_field(self):
        self.__target.execute(self.__hardware)
        self.validate_string_field_was_called_with("platform", self.__hardware.platform)

    def test_execute_validates_numowned_field(self):
        self.__target.execute(self.__hardware)
        self.validate_integer_field_was_called_with("Number owned", self.__hardware.numowned)

    def test_execute_validates_numboxed_field(self):
        self.__target.execute(self.__hardware)
        self.validate_integer_field_was_called_with("Number boxed", self.__hardware.numboxed)