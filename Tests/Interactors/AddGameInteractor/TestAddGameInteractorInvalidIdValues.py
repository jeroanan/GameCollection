from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidIdValues(AddGameValueTest):

    def test_execute_with_game_id_raises_value_error(self):
        game = self.get_game(game_id="id")
        self.assertRaises(ValueError, self.target.execute, game)