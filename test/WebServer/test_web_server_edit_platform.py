"""Unit tests for WebServer EditPlatform endpoint."""
from unittest.mock import Mock
from test.WebServer.web_server_test_base import WebServerTestBase
from ui.handlers.edit_platform_handler import EditPlatformHandler


class TestWebServerEditPlatform(WebServerTestBase):
    """Unit tests for WebServer EditPlatform endpoint."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(EditPlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_editplatform_calls_handler_get_page(self):
        """Tests that the EditPlatform handler's get_page method is called correctly."""
        self.target.default(*("editplatform",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "platformid": "id"
        }
