from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidNumBoxedValues(AddGameValueTest):

    def test_execute_validates_num_boxed_field(self):
        game = self.get_game(num_boxed=1)
        self.target.execute(game)
        self.validate_integer_field_was_called_with("Number of boxed items", 1)
