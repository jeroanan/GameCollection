from unittest.mock import Mock
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWevServerDeleteHardware(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(DeleteHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_delete_hardware_calls_handler(self):
        self.target.deletehardware(**self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "id"
        }
