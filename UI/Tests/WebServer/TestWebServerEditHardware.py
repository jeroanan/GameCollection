from unittest.mock import Mock
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerEditHardware(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(EditHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_edithardware_calls_handler_get_page(self):
        self.target.edithardware(**self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "id"
        }
