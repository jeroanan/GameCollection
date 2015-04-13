from Genre import Genre
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase
from Interactors.Genre.UpdateGenreInteractor import UpdateGenreInteractor


class TestUpdateGenreInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = UpdateGenreInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        genre = Genre()
        self.__target.execute(genre)
        self.persistence.update_genre.assert_called_with(genre)

