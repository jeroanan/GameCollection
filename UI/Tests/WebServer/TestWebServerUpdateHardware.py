from unittest.mock import Mock
from UI.Handlers.UpdateHardwareHandler.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdateHardwareHandler.UpdateHardwareHandlerParams import UpdateHardwareHandlerParams
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerUpdateHardware(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdateHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__id = "id"
        self.__name = "name"
        self.__platform = "platform"
        self.__num_owned = "1"
        self.__num_boxed = "0"
        self.__notes = ""

    def test_updatehardware_calls_handler_get_page(self):

        self.target.updatehardware(id=self.__id, name=self.__name, platform=self.__platform, numcopies=self.__num_owned,
                                   numboxed=self.__num_boxed, notes=self.__notes)

        self.__handler.get_page.assert_called_with(params=self.__get_params())

    def __get_params(self):
        p = UpdateHardwareHandlerParams()
        p.id = self.__id
        p.name = self.__name
        p.platform = self.__platform
        p.num_owned = self.__num_owned
        p.num_boxed = self.__num_boxed
        p.notes = self.__notes
        return p