from unittest.mock import Mock
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerEditHardware(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(EditHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__hardware_id = "id"

    def test_edithardware_calls_handler_get_page(self):
        self.target.edithardware(hardwareid=self.__hardware_id)
        self.__handler.get_page.assert_called_with(self.__hardware_id)
