from unittest.mock import Mock
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerUpdateGame(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdateGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__game_id = "id"
        self.__game_title = "title"
        self.__game_platform = "platform"
        self.__game_num_copies = "1"
        self.__game_num_boxed = "2"
        self.__game_num_manuals = "3"
        self.__game_notes = "notes"

    def test_updategame_calls_handler_get_page(self):
        self.target.updategame(id=self.__game_id, title=self.__game_title, platform=self.__game_platform,
                               numcopies=self.__game_num_copies, numboxed=self.__game_num_boxed,
                               nummanuals=self.__game_num_manuals, notes=self.__game_notes)

        self.__handler.get_page.assert_called_with(id=self.__game_id, title=self.__game_title,
                                                   platform=self.__game_platform, numcopies=self.__game_num_copies,
                                                   numboxed=self.__game_num_boxed, nummanuals=self.__game_num_manuals,
                                                   notes=self.__game_notes)
