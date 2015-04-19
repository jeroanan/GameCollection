from unittest.mock import Mock

from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerSaveHardware(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(SaveHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_savehardware_calls_handler_get_page(self):
        self.target.default(*("savehardware",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "name": "name",
            "platform": "platform",
            "numowned": 1,
            "numboxed": 2,
            "notes": "notes"
        }