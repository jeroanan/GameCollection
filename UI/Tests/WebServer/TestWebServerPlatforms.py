from unittest.mock import Mock

from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerPlatforms(WebServerTestBase):

    def test_platforms_calls_handler_get_page(self):
        handler = Mock(AddPlatformHandler)
        self.target.handler_factory = self.get_handler_factory(handler)
        self.target.default(*("platforms",))
        handler.get_page.assert_called_with({})

    def test_platforms_extra_args(self):
        self.target.default(*("platforms",), **{"spam": "eggs"})