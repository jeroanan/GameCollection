from Interactors.Interactor import Interactor
from Interactors.Search.Params.SearchInteractorParams import SearchInteractorParams
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
        self.persistence.search.assert_called_with(search_term="search", sort_field="title", sort_dir="asc", user_id="userid")

    def __execute(self, search_term="search", sort_field="title", sort_dir="asc", user_id="userid"):
        p = SearchInteractorParams()
        p.search_term = search_term
        p.sort_field = sort_field
        p.sort_direction = sort_dir
        p.user_id = user_id
        self.__target.execute(p)
