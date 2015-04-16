from Interactors.Hardware.GetHardwareDetailsInteractor import GetHardwareDetailsInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetHardwareDetailsInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetHardwareDetailsInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_hardware_id_raises_type_error(self):
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_calls_persistence_method(self):
        self.__execute(hardware_id="platformid", user_id="user_id")
        self.persistence.get_hardware_details.assert_called_with("platformid", "user_id")

    def __execute(self, hardware_id, user_id="userid"):
        self.__target.execute(hardware_id, user_id)