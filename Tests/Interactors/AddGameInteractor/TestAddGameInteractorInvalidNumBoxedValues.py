from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidNumBoxedValues(AddGameValueTest):

    def test_execute_with_none_num_boxed_raises_value_error(self):
        self.__assert_num_boxed_invalid_value(None)

    def test_execute_with_empty_num_boxed_raises_value_error(self):
        self.__assert_num_boxed_invalid_value("")

    def test_execute_with_whitespace_num_boxed_raises_value_error(self):
        self.__assert_num_boxed_invalid_value(" ")

    def test_execute_with_string_num_boxed_raises_value_error(self):
        self.__assert_num_boxed_invalid_value("wrong")

    def test_execute_with_negative_num_boxed_raises_value_error(self):
        self.__assert_num_boxed_invalid_value(-1)

    def test_execute_with_floating_point_num_boxed_raises_value_error(self):
        self.__assert_num_boxed_invalid_value(3.141)

    def __assert_num_boxed_invalid_value(self, num_boxed):
        game = self.get_game(title="Title", platform="Platform", num_boxed=num_boxed)
        self.assertRaises(ValueError, self.target.execute, game)