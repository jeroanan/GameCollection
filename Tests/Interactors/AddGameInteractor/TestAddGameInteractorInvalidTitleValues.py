from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidTitleValues(AddGameValueTest):

    def test_execute_validates_game_title_field(self):
        self.target.execute(self.get_game(title="title"))
        self.assertTrue(self.validate_string_field_was_called_with("Game title", "title"))


