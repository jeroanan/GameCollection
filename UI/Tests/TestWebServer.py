import unittest
from unittest.mock import Mock
from Data.Config import Config

from Interactors import InteractorFactory
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.EditPlatformHandler import EditPlatformHandler
from UI.Handlers.Handler import Handler
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.SearchHandler import SearchHandler
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
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
        handler = Mock(IndexHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        game_sort_field = "title"
        game_sort_direction = "asc"
        hardware_sort_field = "name"
        hardware_sort_direction = "asc"
        self.__target.index(gamesort=game_sort_field, gamesortdir=game_sort_direction, hardwaresort=hardware_sort_field,
                            hardwaresortdir=hardware_sort_direction)

        handler.get_page.assert_called_with(game_sort=game_sort_field, game_sort_direction=game_sort_direction,
                                            hardware_sort=hardware_sort_field,
                                            hardware_sort_direction=hardware_sort_direction)

    def test_add_game_calls_handler_get_page(self):
        handler = Mock(AddGameHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)

        self.__target.addgame()
        handler.get_page.assert_called_with()

    def test_savegame_calls_handler_get_page(self):
        handler = Mock(SaveGameHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)

        title = None
        numcopies = None
        numboxed = None
        nummanuals = None
        platform = ""
        notes = ""
        self.__target.savegame(title=title, numcopies=numcopies, numboxed=numboxed, nummanuals=nummanuals,
                               platform=platform, notes=notes)

        handler.get_page.assert_called_with(title=title, numcopies=numcopies, numboxed=numboxed,
                                            nummanuals=nummanuals, platform=platform, notes=notes)

    def test_addhardware_calls_handler_get_page(self):
        handler = Mock(AddHardwareHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.addhardware()
        handler.get_page.assert_called_with()

    def test_platforms_calls_handler_get_page(self):
        handler = Mock(AddPlatformHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.platforms()
        handler.get_page.assert_called_with()

    def test_addplatform_calls_handler_get_page(self):
        handler = Mock(AddPlatformHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.addplatform("name", "description")
        handler.get_page.assert_called_with(name="name", description="description")

    def test_editplatform_calls_handler_get_page(self):
        handler = Mock(EditPlatformHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.editplatform(platformid="id")
        handler.get_page.assert_called_with("id")

    def test_deleteplatform_calls_handler_get_page(self):
        handler = Mock(DeletePlatformHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.deleteplatform(platformid="id")
        handler.get_page.assert_called_with("id")

    def test_updateplatform_calls_handler_get_page(self):
        handler = Mock(UpdatePlatformHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.updateplatform(id="id", name="name", description="description")
        handler.get_page.assert_called_with(id="id", name="name", description="description")

    def test_editgame_calls_handler_get_page(self):
        handler = Mock(EditGameHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        game_id = "id"
        self.__target.editgame(game_id)
        handler.get_page.assert_called_with(game_id=game_id)

    def test_updategame_calls_handler_get_page(self):
        handler = Mock(UpdateGameHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.updategame(id="id", title="title", platform="platform", numcopies="1", numboxed="2",
                                 nummanuals="3", notes="notes")
        handler.get_page.assert_called_with(id="id", title="title", platform="platform", numcopies="1",
                                            numboxed="2", nummanuals="3", notes="notes")

    def test_deletegame_calls_handler_get_page(self):
        handler = Mock(DeleteGameHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        game_id = "id"
        self.__target.deletegame(gameid=game_id)
        handler.get_page.assert_called_with(game_id)

    def test_savehardware_calls_handler_get_page(self):
        handler = Mock(SaveHardwareHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)

        name = "name"
        platform = "platform"
        num_owned = "numowned"
        num_boxed = "numboxed"
        notes = "notes"

        self.__target.savehardware(name=name, platform=platform, numowned=num_owned, numboxed=num_boxed, notes=notes)
        handler.get_page.assert_called_with(name=name, platform=platform, numowned=num_owned, numboxed=num_boxed,
                                            notes=notes)

    def test_edithardware_calls_handler_get_page(self):
        handler = Mock(EditHardwareHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        self.__target.edithardware(hardwareid="id")
        handler.get_page.assert_called_with("id")

    def test_updatehardware_calls_handler_get_page(self):
        handler = Mock(UpdateHardwareHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)

        id = "id"
        name = "name"
        platform = "platform"
        numcopies = "1"
        numboxed = "0"
        notes = ""

        self.__target.updatehardware(id=id, name=name, platform=platform, numcopies=numcopies, numboxed=numboxed,
                                     notes=notes)

        handler.get_page.assert_called_with(id=id, name=name, platform=platform, numowned=numcopies,
                                            numboxed=numboxed, notes=notes)

    def test_delete_hardware_calls_handler(self):
        handler = Mock(DeleteHardwareHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        hardware_id = "id"
        self.__target.deletehardware(hardwareid=hardware_id)
        handler.get_page.assert_called_with(hardware_id=hardware_id)

    def test_allgames_calls_handler_get_page(self):
        handler = Mock(AllGamesHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        sort_field = "title"
        sort_dir = "asc"
        platform = None
        self.__target.allgames(gamesort=sort_field, gamesortdir=sort_dir, platform=platform)
        handler.get_page.assert_called_with(sort_field=sort_field, sort_direction=sort_dir, platform=platform)

    def test_search_calls_handler_get_page(self):
        handler = Mock(SearchHandler)
        self.__target.handler_factory = self.__get_handler_factory(handler)
        search_term = "search"
        game_sort = ""
        sort_dir = "asc"
        self.__target.search(searchterm=search_term, gamesort=game_sort, gamesortdir=sort_dir)
        handler.get_page.assert_called_with(search_term=search_term, sort_field=game_sort, sort_dir=sort_dir)

    def __get_handler_factory(self, handler):
        handler_factory = Mock(HandlerFactory)
        handler_factory.create = Mock(return_value=handler)
        return handler_factory