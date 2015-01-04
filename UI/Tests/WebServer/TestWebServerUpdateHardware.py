from unittest.mock import Mock

from UI.Handlers.UpdateHardwareHandler.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerUpdateHardware(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdateHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_updatehardware_calls_handler_get_page(self):
        self.target.updatehardware(**self.__get_params())
        self.__handler.get_page.assert_called_with(params=self.__get_params())

    def __get_params(self):
        return {
            "id": "id",
            "name": "name",
            "platform": "platform",
            "numowned": 1,
            "numboxed": 0,
            "notes": "notes"
        }