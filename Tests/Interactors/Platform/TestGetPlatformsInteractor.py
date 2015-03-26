from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetPlatformsInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetPlatformsInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        self.__target = GetPlatformsInteractor()
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        self.__target.execute()
        self.assertTrue(self.persistence.get_platforms.called)