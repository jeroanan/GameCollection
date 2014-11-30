from Interactors.Interactor import Interactor
from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractor(AddGameValueTest):

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.target.execute(self.get_game())
        self.assertTrue(self.persistence.add_game.called)

    def test_execute_with_null_game_raises_type_error(self):
        self.assertRaises(TypeError, self.target.execute, None)

    def test_execute_validates_num_boxed_field(self):
        self.target.execute(self.get_game(num_boxed=1))
        self.validate_integer_field_was_called_with("Number of boxed items", 1)

    def test_execute_validates_num_copies_field(self):
        self.target.execute(self.get_game(num_copies=1))
        self.validate_integer_field_was_called_with("Number of copies", 1)

    def test_execute_validates_num_manuals_field(self):
        self.target.execute(self.get_game(num_manuals=1))
        self.validate_integer_field_was_called_with("Number of manuals", 1)

    def test_execute_with_game_id_raises_value_error(self):
        game = self.get_game(game_id="id")
        self.assertRaises(ValueError, self.target.execute, game)
