from Genre import Genre
from Interactors.Genre.AddGenreInteractor import AddGenreInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestAddGenreInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = AddGenreInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        genre = Genre()
        self.__target.execute(genre=genre)
        self.persistence.add_genre.assert_called_with(genre)

    def test_execute_with_none_genre_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_title_field(self):
        genre = Genre()
        genre.name = "Genre"
        self.__target.execute(genre)
        self.assertTrue(self.validate_string_field_was_called_with("Name", genre.name))