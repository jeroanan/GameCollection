from Interactors.Interactor import Interactor
from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractor(AddGameValueTest):

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.target, Interactor)

    def test_execute_calls_persistence_method(self):
        game = self.get_game(title="Title", platform="Platform")
        self.target.execute(game)
        self.assertTrue(self.persistence.add_game.called)

    def test_execute_with_null_game_raises_type_error(self):
        self.assertRaises(TypeError, self.target.execute, None)