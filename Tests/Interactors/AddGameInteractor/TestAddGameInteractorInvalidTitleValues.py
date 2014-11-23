from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidTitleValues(AddGameValueTest):

    def test_execute_with_none_title_raises_value_error(self):
        self.__assert_title_invalid_value(None)

    def test_execute_with_empty_title_raises_value_error(self):
        self.__assert_title_invalid_value("")

    def test_execute_with_whitespace_title_raises_value_error(self):
        self.__assert_title_invalid_value(" ")

    def __assert_title_invalid_value(self, title):
        game = self.get_game(title=title)
        self.assertRaises(ValueError, self.target.execute, game)

