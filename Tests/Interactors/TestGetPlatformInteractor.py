from Interactors.GetPlatformInteractor import GetPlatformInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetPlatformInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetPlatformInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_get_platform(self):
        self.__target.execute(platform_id="platformId")
        self.assertTrue(self.persistence.get_platform.called)


