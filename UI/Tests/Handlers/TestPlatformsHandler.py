import unittest
from unittest.mock import Mock

from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.Platform.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.TemplateRenderer import TemplateRenderer


class TestPlatformsHandler(unittest.TestCase):

    def setUp(self):
        self.__get_platforms_interactor = Mock(GetPlatformsInteractor)
        self.__get_suggested_platforms_interactor = Mock(GetSuggestedPlatformsInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__interactor_factory_create())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = PlatformsHandler(self.__interactor_factory, self.__renderer)

    def __interactor_factory_create(self):
        return [self.__get_platforms_interactor, self.__get_suggested_platforms_interactor]

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor_execute(self):
        self.__get_page()
        self.assertTrue(self.__get_platforms_interactor.execute.called)

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.assertTrue(self.__renderer.render.called)

    def test_get_page_creates_get_suggested_platforms_interactor(self):
        self.__get_page()
        self.__interactor_factory.create.assert_called_with("GetSuggestedPlatformsInteractor")

    def test_get_page_executes_get_suggested_platforms_interactor(self):
        self.__get_page()
        self.__get_suggested_platforms_interactor.execute.assert_called_with()

    def __get_page(self):
        self.__target.get_page({})