from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGamesInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetGamesInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        number_of_games = 10
        sort_field = None
        sort_direction = "asc"
        platform = ""
        self.__target.execute(number_of_games=number_of_games, sort_field=sort_field, sort_direction=sort_direction,
                              platform=platform)
        self.__target.persistence.get_all_games.assert_was_called_with()

    def test_execute_with_platform_calls_get_all_games_for_platform_persistence_method(self):
        number_of_games = 10
        sort_field = None
        sort_direction = "asc"
        platform = "platform"
        self.__target.execute(number_of_games=number_of_games, sort_field=sort_field, sort_direction=sort_direction,
                              platform=platform)
        self.__target.persistence.get_all_games_for_platform.assert_was_called_with()