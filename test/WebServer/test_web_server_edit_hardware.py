"""Unit tests for WebServer EditHardware endpoint."""
from unittest.mock import Mock
from test.WebServer.web_server_test_base import WebServerTestBase
from ui.Handlers.edit_hardware_handler import EditHardwareHandler


class TestWebServerEditHardware(WebServerTestBase):
    """Unit tests for WebServer EditHardware endpoint."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(EditHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_edithardware_calls_handler_get_page(self):
        """Tests that the EditHardware handler's get_page method is called correctly."""
        self.target.default(*("edithardware",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "id"
        }
