from Interactors.GetGenresInteractor import GetGenresInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGenresInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetGenresInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute()
        self.persistence.get_genres.assert_called_with()