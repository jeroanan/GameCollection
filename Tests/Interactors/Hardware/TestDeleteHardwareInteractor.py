from Interactors.Hardware.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestDeleteHardwareInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = DeleteHardwareInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field
        self.__target.validate_integer_field = self.validate_integer_field

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_hardware_id_raises_type_error(self):
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_validates_id_field(self):
        self.__execute("id")
        self.validate_string_field_was_called_with("Hardware Id", "id")

    def test_execute_calls_persistence_method(self):
        hardwareid = "hardwareid"
        user_id = "user_id"
        self.__execute(hardware_id=hardwareid, user_id=user_id)
        self.persistence.delete_hardware.assert_called_with(hardwareid, user_id)

    def __execute(self, hardware_id, user_id="userid"):
        self.__target.execute(hardware_id, user_id)