import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.InteractorFactory import InteractorFactory
from Tests.Interactors.TestUpdatePlatformInteractor import UpdatePlatformInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.TemplateRenderer import TemplateRenderer


class TestUpdatePlatformHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(UpdatePlatformInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = UpdatePlatformHandler(self.__interactor_factory, self.__renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(id="id", name="name", description="descripooin")
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_causes_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, id="id", name="name", description="description")

