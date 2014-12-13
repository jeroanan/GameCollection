from Interactors.GetGenreInteractor import GetGenreInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGenreInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetGenreInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute(game_id="id")
        self.persistence.get_genre_details.assert_called_with("id")