from unittest.mock import Mock
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
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

        self.__handler.get_page.assert_called_with(name=self.__name, platform=self.__platform,
                                                   numowned=self.__num_owned, numboxed=self.__num_boxed,
                                                   notes=self.__notes)
