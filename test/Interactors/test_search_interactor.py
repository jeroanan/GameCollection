"""Unit tests for SearchInteractor"""

from test.Interactors.interactor_test_base import InteractorTestBase
from interactors.interactor import Interactor
from interactors.search.Params.search_interactor_params import SearchInteractorParams
from interactors.search.search_interactor import SearchInteractor


class TestSearchInteractor(InteractorTestBase):
    """Unit tests for SearchInteractor"""

    def setUp(self):
        super().setUp()
        self.__target = SearchInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        """Test that SearchInteractor is a subclass of Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that execute calls the persistence search method with correct parameters"""
        self.__execute()
        self.persistence.search.assert_called_with(
            search_term="search",
            sort_field="title",
            sort_dir="asc",
            user_id="userid")

    def __execute(self, search_term="search", sort_field="title", sort_dir="asc", user_id="userid"):
        p = SearchInteractorParams()
        p.search_term = search_term
        p.sort_field = sort_field
        p.sort_direction = sort_dir
        p.user_id = user_id
        self.__target.execute(p)
