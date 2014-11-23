from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidNumManualsValues(AddGameValueTest):

    def test_execute_with_none_num_manuals_raises_value_error(self):
        self.__assert_num_manuals_invalid_value(None)

    def test_execute_with_empty_num_manuals_raises_value_error(self):
        self.__assert_num_manuals_invalid_value("")

    def test_execute_with_whitespace_num_manuals_raises_value_err(self):
        self.__assert_num_manuals_invalid_value(" ")

    def test_execute_with_string_num_manuals_raises_value_error(self):
        self.__assert_num_manuals_invalid_value("wrong")

    def test_execute_with_negative_num_manuals_raises_value_error(self):
        self.__assert_num_manuals_invalid_value(-1)

    def test_execute_with_floating_point_num_manuals_raises_value_error(self):
        self.__assert_num_manuals_invalid_value(3.141)

    def __assert_num_manuals_invalid_value(self, num_manuals):
        game = self.get_game(title="Title", platform="Platform", num_manuals=num_manuals)
        self.assertRaises(ValueError, self.target.execute, game)