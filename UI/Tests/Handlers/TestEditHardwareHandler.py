import cherrypy
import unittest
from unittest.mock import Mock

from Hardware import Hardware
from Interactors.Hardware.GetHardwareInteractor import GetHardwareDetailsInteractor
from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestEditHardwareHandler(unittest.TestCase):

    def setUp(self):
        def interactors():
            return [get_hardware_details_interactor, get_platforms_interactor]
        self.__hardware = Hardware()
        self.__platforms = [Platform()]
        get_hardware_details_interactor = Mock(GetHardwareDetailsInteractor)
        get_hardware_details_interactor.execute = Mock(return_value=self.__hardware)
        get_platforms_interactor = Mock(GetPlatformsInteractor)
        get_platforms_interactor.execute = Mock(return_value=self.__platforms)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=interactors())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditHardwareHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_calls_renderer(self):
        self.__get_page()
        self.__renderer.render.assert_called_with("edithardware.html", title="Edit Hardware", hardware=self.__hardware, 
                                                  platforms=self.__platforms, hardware_found=True)

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__get_page)
        
    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__get_page)

    def __get_page(self):
        self.__target.get_page(self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "hardwareid"
        }

    def test_get_page_empty_args(self):
        self.__target.get_page({"": ""})
