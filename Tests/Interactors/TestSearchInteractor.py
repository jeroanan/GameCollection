from Interactors.Interactor import Interactor
from Interactors.SearchInteractor import SearchInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestSearchInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = SearchInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute(self):
        self.__target.execute(search_term="search")

    def test_execute_calls_persistence_method(self):
        self.__target.execute(search_term="search")
        self.persistence.search.assert_called_with(search_term="search")
