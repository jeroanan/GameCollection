from Interactors.Game.GetGamesInteractor import GetGamesInteractor
from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGamesInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetGamesInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_calls_persistence_method(self):
        self.__execute()
        self.persistence.get_all_games.assert_was_called_with(self.__get_params())

    def test_with_platform_calls_get_all_games_for_platform_persistence_method(self):
        self.__execute()
        self.__target.persistence.get_all_games_for_platform.assert_was_called_with(self.__get_params())
        
    def test_user_id_not_set_gives_value_error(self):
        p = self.__get_params()
        p.user_id = None
        self.assertRaises(ValueError, self.__target.execute, p)

    def __execute(self):
        self.__target.execute(self.__get_params())
        
    def __get_params(self):
        p = GetGamesInteractorParams()        
        p.number_of_games = 10
        p.sort_field = None
        p.sort_direction = "asc"
        p.platform = "platform"
        p.user_id = "1234"
        return p
        
