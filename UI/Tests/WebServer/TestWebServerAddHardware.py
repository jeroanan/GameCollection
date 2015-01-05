from unittest.mock import Mock
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerAddHardware(WebServerTestBase):

    def test_addhardware_calls_handler_get_page(self):
        handler = Mock(AddHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(handler)
        self.target.addhardware()
        handler.get_page.assert_called_with()

    def test_addhardware_extra_args(self):
        self.target.addhardware(**{"spam": "eggs"})