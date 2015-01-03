from unittest.mock import Mock
from UI.Handlers.SaveGameHandler.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveGameHandler.SaveGameHandlerParams import SaveGameHandlerParams
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerSaveGame(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__title = None
        self.__num_copies = None
        self.__num_boxed = None
        self.__num_manuals = None
        self.__platform = ""
        self.__notes = ""
        self.__handler = Mock(SaveGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_savegame_calls_handler_get_page(self):
        self.target.savegame(title=self.__title, numcopies=self.__num_copies, numboxed=self.__num_boxed,
                             nummanuals=self.__num_manuals, platform=self.__platform, notes=self.__notes)

        self.__handler.get_page.assert_called_with(params=self.__get_params())

    def __get_params(self):
        params = SaveGameHandlerParams()
        params.title = self.__title
        params.num_copies = self.__num_copies
        params.num_boxed = self.__num_boxed
        params.num_manuals = self.__num_manuals
        params.platform = self.__platform
        params.notes = self.__notes
        return params