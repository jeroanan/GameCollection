from Interactors.Game.CountGamesInteractor import CountGamesInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestCountGamesInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = CountGamesInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute()
        self.persistence.count_games.assert_called_with()
