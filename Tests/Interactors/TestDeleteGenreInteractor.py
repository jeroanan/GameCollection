from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class DeleteGenreInteractor(Interactor):

    def execute(self, genre_id):
        self.persistence.delete_genre(genre_id)


class TestDeleteGenreInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = DeleteGenreInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute(self):
        self.__target.execute(genre_id="id")

    def test_execute_calls_persistence(self):
        self.__target.execute(genre_id="id")
        self.persistence.delete_genre.assert_called_with("id")