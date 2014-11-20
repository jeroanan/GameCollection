import unittest
from unittest.mock import Mock
from Interactors.GetPlatformInteractor import GetPlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.EditPlatformHandler import EditPlatformHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer

class TestEditPlatformHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(GetPlatformInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditPlatformHandler(self.__interactor_factory, self.__renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor_execute_method(self):
        self.__target.get_page(platform_id="platformid")
        self.__interactor.execute.assert_called_with("platformid")

    def test_get_page_calls_renderer(self):
        self.__target.get_page(platform_id="platformid")
        self.assertTrue(self.__renderer.render.called)
