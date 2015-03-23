import unittest
from unittest.mock import Mock

import cherrypy
from Game import Game

from Interactors.DeleteGameInteractor import DeleteGameInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestDeleteGameHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(DeleteGameInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteGameHandler(self.__interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor_execute(self):
        self.__target.get_page(self.__get_args())
        self.__interactor.execute.assert_called_with(self.__get_game())

    def __get_game(self):
        g = Game()
        g.id = "id"
        return g

    def __get_args(self):
        return {
            "gameid": "id"
        }

    def test_get_page_empty_args(self):
        self.__target.get_page({"": ""})