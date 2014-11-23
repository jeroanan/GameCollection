from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidPlatformsValues(AddGameValueTest):

    def test_execute_with_none_platform_raises_value_error(self):
        self.__assert_platform_invalid_value(None)

    def test_execute_with_empty_platform_raises_value_error(self):
        self.__assert_platform_invalid_value("")

    def test_execute_with_whitespace_platform_raises_value_error(self):
        self.__assert_platform_invalid_value(" ")

    def __assert_platform_invalid_value(self, platform):
        game = self.get_game(title="title", platform=platform)
        self.assertRaises(ValueError, self.target.execute, game)