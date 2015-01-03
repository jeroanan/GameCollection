from unittest.mock import Mock
from UI.Handlers.SaveHardwareHandler.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.SaveHardwareHandler.SaveHardwareHandlerParams import SaveHardwareHandlerParams
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerSaveHardware(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(SaveHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__name = "name"
        self.__platform = "platform"
        self.__num_owned = "numowned"
        self.__num_boxed = "numboxed"
        self.__notes = "notes"

    def test_savehardware_calls_handler_get_page(self):
        self.target.savehardware(name=self.__name, platform=self.__platform, numowned=self.__num_owned,
                                 numboxed=self.__num_boxed, notes=self.__notes)

        self.__handler.get_page.assert_called_with(params=self.__get_params())

    def __get_params(self):
        p = SaveHardwareHandlerParams()
        p.name = self.__name
        p.platform = self.__platform
        p.num_owned = self.__num_owned
        p.num_boxed = self.__num_boxed
        p.notes = self.__notes
        return p