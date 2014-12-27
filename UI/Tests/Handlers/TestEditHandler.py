import unittest
from unittest.mock import Mock
from Interactors.GetGameInteractor import GetGameInteractor
from Interactors.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestEditHandler(unittest.TestCase):

    def setUp(self):
        self.__renderer = Mock(TemplateRenderer)
        self.__get_game_interactor = Mock(GetGameInteractor)
        self.__get_platforms_interactor = Mock(GetPlatformsInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__get_interactor())
        self.__target = EditGameHandler(self.__interactor_factory, self.__renderer)

    def __get_interactor(self):
        return [self.__get_game_interactor, self.__get_platforms_interactor]

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_renderer(self):
        self.__target.get_page(game_id="game_id")
        self.assertTrue(self.__renderer.render.called)

    def test_get_page_calls_interactor_execute(self):
        self.__target.get_page(game_id="game_id")
        self.assertTrue(self.__get_game_interactor.execute.called)

    def test_get_page_calls_get_platforms_interactor_execute(self):
        self.__target.get_page("game_id")
        self.assertTrue(self.__get_platforms_interactor.execute.called)
