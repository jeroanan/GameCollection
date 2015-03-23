from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.AllGamesHandler.AllGamesHandler import AllGamesHandler
from UI.Handlers.AllHardwareHandler import AllHardwareHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.IndexHandler.IndexHandler import IndexHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.SearchHandler.SearchHandler import SearchHandler
from UI.Handlers.SortGamesHandler import SortGamesHandler
from UI.Handlers.SortHardwareHandler import SortHardwareHandler
from UI.Handlers.UpdateGameHandler.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdateHardwareHandler.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdatePlatformHandler.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Tests.Handlers.TestEditPlatformHandler import EditPlatformHandler


class HandlerFactory(object):

    def __init__(self, interactor_factory, renderer, config):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer

        self.__handlers = {
            "index": IndexHandler(self.__interactor_factory, self.__renderer, config),
            "savegame": SaveGameHandler(self.__interactor_factory, self.__renderer),
            "addgame": AddGameHandler(self.__interactor_factory, self.__renderer),
            "addhardware": AddHardwareHandler(self.__interactor_factory, self.__renderer),
            "platforms": PlatformsHandler(self.__interactor_factory, self.__renderer),
            "addplatform": AddPlatformHandler(self.__interactor_factory, self.__renderer),
            "editgame": EditGameHandler(self.__interactor_factory, self.__renderer),
            "updategame": UpdateGameHandler(self.__interactor_factory, self.__renderer),
            "deletegame": DeleteGameHandler(self.__interactor_factory, self.__renderer),
            "savehardware": SaveHardwareHandler(self.__interactor_factory, self.__renderer),
            "editplatform": EditPlatformHandler(self.__interactor_factory, self.__renderer),
            "updateplatform": UpdatePlatformHandler(self.__interactor_factory, self.__renderer),
            "deleteplatform": DeletePlatformHandler(self.__interactor_factory, self.__renderer),
            "edithardware": EditHardwareHandler(self.__interactor_factory, self.__renderer),
            "updatehardware": UpdateHardwareHandler(self.__interactor_factory, self.__renderer),
            "deletehardware": DeleteHardwareHandler(self.__interactor_factory, self.__renderer),
            "allgames": AllGamesHandler(self.__interactor_factory, self.__renderer),
            "search": SearchHandler(self.__interactor_factory, self.__renderer),
            "allhardware": AllHardwareHandler(self.__interactor_factory, self.__renderer),
            "sortgames": SortGamesHandler(self.__interactor_factory, self.__renderer),
            "sorthardware": SortHardwareHandler(self.__interactor_factory, self.__renderer)
        }

    def create(self, handler_type):
        if handler_type in self.__handlers:
            return self.__handlers[handler_type]

        raise UnrecognisedHandlerException
