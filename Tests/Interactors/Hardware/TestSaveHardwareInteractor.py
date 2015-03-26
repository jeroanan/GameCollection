from Interactors.Interactor import Interactor
from Interactors.Hardware.SaveHardwareInteractor import SaveHardwareInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestSaveHardwareInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = SaveHardwareInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field
        self.__hardware = self.get_hardware(name="name", platform="platform", num_owned=1, num_boxed=1)

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        self.__target.execute(self.get_hardware())
        self.assertTrue(self.persistence.save_hardware.called)

    def test_execute_with_null_hardware_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_id_set_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.get_hardware(hardware_id="id"))

    def test_execute_validates_name_field(self):
        self.__target.execute(self.__hardware)
        self.assertTrue(self.validate_string_field_was_called_with("Hardware name", self.__hardware.name))

    def test_execute_validates_platform_field(self):
        self.__target.execute(self.__hardware)
        self.assertTrue(self.validate_string_field_was_called_with("Platform", self.__hardware.platform))

    def test_execute_validates_numowned_field(self):
        self.__target.execute(self.__hardware)
        self.assertTrue(self.validate_integer_field_was_called_with("Number owned", self.__hardware.num_owned))

    def test_execute_validates_numboxed_field(self):
        self.__target.execute(self.__hardware)
        self.assertTrue(self.validate_integer_field_was_called_with("Number boxed", self.__hardware.num_boxed))

