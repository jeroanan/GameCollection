import unittest
from unittest.mock import Mock
import cherrypy
from Game import Game
from Interactors.InteractorFactory import InteractorFactory
from Interactors.UpdateGameInteractor import UpdateGameInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.UpdateGameHandler.UpdateGameHandler import UpdateGameHandler
from UI.TemplateRenderer import TemplateRenderer


class TestUpdateGameHandler(unittest.TestCase):
    def setUp(self):
        renderer = Mock(TemplateRenderer)
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(UpdateGameInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = UpdateGameHandler(interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor_execute(self):
        try:
            self.__target.get_page(params=self.__get_params())
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with(game=self.__get_game())

    def __get_game(self):
        g = Game()
        g.id = "id"
        g.title = "title"
        g.num_copies = 1
        g.num_boxed = 2
        g.num_manuals = 3
        g.platform = "platform"
        g.notes = "notes"
        return g

    def test_get_page_does_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, params=self.__get_params())

    def __get_params(self):
        return {
            "id": "id",
            "title": "title",
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "platform": "platform",
            "notes": "notes"
        }

    def test_get_page_empty_params(self):
        try:
            self.__target.get_page({"": ""})
        except cherrypy.HTTPRedirect:
            pass
