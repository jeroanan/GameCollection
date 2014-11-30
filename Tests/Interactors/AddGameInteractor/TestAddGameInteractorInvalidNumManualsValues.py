from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidNumManualsValues(AddGameValueTest):

    def test_execute_validates_num_manuals_field(self):
        game = self.get_game(num_manuals=1)
        self.target.execute(game)
        self.validate_integer_field_was_called_with("Number of manuals", 1)
