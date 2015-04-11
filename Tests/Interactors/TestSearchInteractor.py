from Interactors.Interactor import Interactor
from Interactors.Search.SearchInteractor import SearchInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestSearchInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = SearchInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__execute()
        self.persistence.search.assert_called_with(search_term="search", sort_field="title", sort_dir="asc")

    def __execute(self, search_term="search", sort_field="title", sort_dir="asc"):
        self.__target.execute(search_term=search_term, sort_field=sort_field, sort_dir=sort_dir)
