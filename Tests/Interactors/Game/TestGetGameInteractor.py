from Interactors.Game.GetGameInteractor import GetGameInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGameInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetGameInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_game_id_raises_value_error(self):
        self.assertRaises(ValueError, self.__execute, None)

    def test_execute_calls_persistence(self):
        self.__execute("gameid", "user")
        self.persistence.get_game.assert_called_with("gameid", "user")

    def __execute(self, game_id, user_id="userid"):
        self.__target.execute(game_id, user_id)