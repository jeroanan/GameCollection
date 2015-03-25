from Interactors.Game.DeleteGameInteractor import DeleteGameInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestDeleteGameInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = DeleteGameInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute(self.get_game(game_id="1337"))
        self.assertTrue(self.persistence.delete_game.called)

    def test_execute_with_none_game_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_id_field(self):
        game = self.get_game(game_id="id")
        self.__target.execute(game)
        self.assertTrue(self.validate_string_field_was_called_with("Game id", game.id))