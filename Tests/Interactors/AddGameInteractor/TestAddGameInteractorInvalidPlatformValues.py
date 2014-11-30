from Tests.Interactors.AddGameInteractor.AddGameValueTest import AddGameValueTest


class TestAddGameInteractorInvalidPlatformsValues(AddGameValueTest):

    def test_execute_validates_platform_field(self):
        self.target.execute(self.get_game(platform="platform"))
        self.assertTrue(self.validate_string_field_was_called_with("Platform", "platform"))
