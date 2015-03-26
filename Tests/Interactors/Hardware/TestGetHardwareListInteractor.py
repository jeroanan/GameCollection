from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetHardwareListInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetHardwareListInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        self.__target.execute(sort_field="name", sort_direction="asc")
        self.persistence.get_hardware_list.assert_called_with(sort_field="name", sort_direction="asc")