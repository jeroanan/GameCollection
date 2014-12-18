from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGamesInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetGamesInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute(number_of_games=10)
        self.persistence.get_all_games.assert_was_called_with()