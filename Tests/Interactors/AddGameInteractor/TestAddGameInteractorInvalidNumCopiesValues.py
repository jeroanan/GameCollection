from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidNumCopiesValues(AddGameValueTest):

    def test_execute_validates_num_copies_field(self):
        game = self.get_game(num_copies=1)
        self.target.execute(game)
        self.validate_integer_field_was_called_with("Number of copies", 1)
