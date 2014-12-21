import unittest
from unittest.mock import Mock
from Data.Config import Config

from Interactors import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.TemplateRenderer import TemplateRenderer
from UI.WebServer import WebServer


class TestWebServer(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__renderer = Mock(TemplateRenderer)
        self.__handler_factory = Mock(HandlerFactory)
        self.__handler = Mock(Handler)
        self.__handler_factory.create = Mock(return_value=self.__handler)
        self.__config = Mock(Config)

        self.__target = WebServer(interactor_factory=self.__interactor_factory, renderer=self.__renderer,
                                  config=self.__config)

        self.__target.handler_factory = self.__handler_factory

    def test_instantiate_without_renderer_uses_default(self):
        t = WebServer(self.__interactor_factory)
        self.assertIsInstance(t.renderer, TemplateRenderer)

    def test_index_calls_handler_get_page(self):
        sort_field = "title"
        sort_direction = "asc"
        self.__target.index(gamesort=sort_field, gamesortdir=sort_direction)
        self.__handler.get_page.assert_called_with(game_sort=sort_field, game_sort_direction=sort_direction)

    def test_add_game_calls_handler_get_page(self):
        self.__target.addgame()
        self.__handler.get_page.assert_called_with()

    def test_savegame_calls_handler_get_page(self):
        self.__target.savegame(None, None, None, None)
        self.assertTrue(self.__handler.get_page.called)

    def test_addhardware_calls_handler_get_page(self):
        self.__target.addhardware()
        self.__handler.get_page.assert_called_with()

    def test_platforms_calls_handler_get_page(self):
        self.__target.platforms()
        self.__handler.get_page.assert_called_with()

    def test_addplatform_calls_handler_get_page(self):
        self.__target.addplatform("name", "description")
        self.assertTrue(self.__handler.get_page.called)

    def test_editplatform_calls_handler_get_page(self):
        self.__target.editplatform(platformid="id")
        self.__handler.get_page.assert_called_with("id")

    def test_deleteplatform_calls_handler_factory(self):
        self.__target.deleteplatform(platformid="id")
        self.__handler_factory.create.assert_called_with("DeletePlatformHandler")

    def test_deleteplatform_calls_handler_get_page(self):
        self.__target.deleteplatform(platformid="id")
        self.__handler.get_page.assert_called_with("id")

    def test_updateplatform_calls_handler_get_page(self):
        self.__target.updateplatform(id="id", name="name", description="description")
        self.assertTrue(self.__handler.get_page.called)

    def test_editgame_calls_handler_get_page(self):
        self.__target.editgame("id")
        self.assertTrue(self.__handler.get_page.called)

    def test_updategame_calls_handler_get_page(self):
        self.__target.updategame(id="id", title="title", platform="platform", numcopies="1", numboxed="2",
                                 nummanuals="3")
        self.__handler.get_page.assert_called_with(id="id", title="title", platform="platform", numcopies="1",
                                                   numboxed="2", nummanuals="3")

    def test_deletegame_calls_handler_get_page(self):
        self.__target.deletegame(gameid="id")
        self.__handler.get_page.assert_called_with("id")

    def test_savehardware_calls_handler_get_page(self):
        self.__target.savehardware(name="name", platform="platform", numowned="numowned", numboxed="numboxed")
        self.__handler.get_page.assert_called_with(name="name", platform="platform", numowned="numowned",
                                                 numboxed="numboxed")

    def test_edithardware_calls_handler_get_page(self):
        self.__target.edithardware(hardwareid="id")
        self.__handler.get_page.assert_called_with("id")

    def test_updatehardware_calls_handler_factory(self):
        self.__target.updatehardware(id="id", name="name", platform="platform", numcopies="1", numboxed="0")
        self.__handler_factory.create.assert_called_with("UpdateHardwareHandler")

    def test_updatehardware_calls_handler_get_page(self):
        self.__target.updatehardware(id="id", name="name", platform="platform", numcopies="1", numboxed="0")
        self.__handler.get_page.assert_called_with(id="id", name="name", platform="platform", numowned="1", numboxed="0")

    def test_deletehardware_calls_handler_factory(self):
        self.__target.deletehardware(hardwareid="id")
        self.__handler_factory.create.assert_called_with("DeleteHardwareHandler")

    def test_delete_hardware_calls_handler(self):
        self.__target.deletehardware(hardwareid="id")
        self.__handler.get_page.assert_called_with(hardware_id="id")

    def test_genres_calls_handler(self):
        self.__target.genres()
        self.__handler.get_page.assert_called_with()

    def test_addgenre_calls_handler_factory(self):
        self.__target.addgenre(name="name", description="description")
        self.__handler_factory.create.assert_called_with("AddGenreHandler")

    def test_add_genre_calls_handler_get_page(self):
        self.__target.addgenre(name="name", description="description")
        self.__handler.get_page.assert_called_with(name="name", description="description")

    def test_edit_genre_handler_calls_handler_factory(self):
        self.__target.editgenre(genreid="id")
        self.__handler_factory.create.assert_called_with("EditGenreHandler")

    def test_edit_genre_handler_calls_handler_get_page(self):
        self.__target.editgenre(genreid="id")
        self.__handler.get_page.assert_called_with(genre_id="id")

    def test_update_genre_calls_handler_factory(self):
        self.__target.updategenre(id="id", name="name", description="description")
        self.__handler_factory.create.assert_called_with("UpdateGenreHandler")
        self.__handler.get_page.assert_called_with(id="id", name="name", description="description")

    def test_delete_genre_calls_handler_factory(self):
        self.__target.deletegenre(genreid="id")
        self.__handler_factory.create.assert_called_with("DeleteGenreHandler")

    def test_delete_genre_calls_handler_get_page(self):
        self.__target.deletegenre(genreid="id")
        self.__handler.get_page.assert_called_with(genre_id="id")

    def test_allgames_calls_handler_factory(self):
        self.__target.allgames()
        self.__handler_factory.create.assert_called_with("AllGamesHandler")

    def test_allgames_calls_handler_get_page(self):
        sort_field = "title"
        sort_dir = "asc"
        self.__target.allgames(gamesort=sort_field, gamesortdir=sort_dir)
        self.__handler.get_page.assert_called_with(sort_field=sort_field, sort_direction=sort_dir)