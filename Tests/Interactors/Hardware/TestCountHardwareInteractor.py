from unittest.mock import Mock

from AbstractPersistence import AbstractPersistence
from Interactors.Hardware.CountHardwareInteractor import CountHardwareInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestCountHardwareInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = CountHardwareInteractor()
        self.__persistence = Mock(AbstractPersistence)
        self.__target.persistence = self.__persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute()
        self.__persistence.count_hardware.assert_called_with()