import cherrypy
import unittest
from unittest.mock import Mock

from Hardware import Hardware
from Interactors.Hardware import GetHardwareListInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SortHardwareHandler import SortHardwareHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSortHardwareHandler(unittest.TestCase):

    def setUp(self):
        self.__hardware = [Hardware()]
        self.__interactor = Mock(GetHardwareListInteractor)
        self.__interactor.execute = Mock(return_value=self.__hardware)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = SortHardwareHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_executes_renderer(self):
        args = self.__get_args()
        self.__target.get_page(args)
        self.__renderer.render.assert_called_with("hardware.html", hardware=self.__hardware,
                                                  hw_sort_field=args["field"], hw_sort_dir=args["sortdir"])

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_args())

    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_args())

    def __get_args(self):
        return {"field": "title", "sortdir": "asc", "numrows": 2}
