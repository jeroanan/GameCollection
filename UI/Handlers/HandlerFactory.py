from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeleteGenreHandler import DeleteGenreHandler
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.EditGenreHandler import EditGenreHandler
from UI.Handlers.EditHandler import EditHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.GetGenresHandler import GetGenresHandler
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdateGenreHandler import UpdateGenreHandler
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Tests.Handlers.TestAddGenreHandler import AddGenreHandler
from UI.Tests.Handlers.TestEditPlatformHandler import EditPlatformHandler


class HandlerFactory(object):

    def __init__(self, interactor_factory, renderer, config):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer

        self.__handlers = {
            "IndexHandler": IndexHandler(self.__interactor_factory, self.__renderer, config),
            "SaveGameHandler": SaveGameHandler(self.__interactor_factory, self.__renderer),
            "AddGameHandler": AddGameHandler(self.__interactor_factory, self.__renderer),
            "AddHardwareHandler": AddHardwareHandler(self.__interactor_factory, self.__renderer),
            "PlatformsHandler": PlatformsHandler(self.__interactor_factory, self.__renderer),
            "AddPlatformHandler": AddPlatformHandler(self.__interactor_factory, self.__renderer),
            "EditGameHandler": EditHandler(self.__interactor_factory, self.__renderer),
            "UpdateGameHandler": UpdateGameHandler(self.__interactor_factory, self.__renderer),
            "DeleteGameHandler": DeleteGameHandler(self.__interactor_factory, self.__renderer),
            "SaveHardwareHandler": SaveHardwareHandler(self.__interactor_factory, self.__renderer),
            "EditPlatformHandler": EditPlatformHandler(self.__interactor_factory, self.__renderer),
            "UpdatePlatformHandler": UpdatePlatformHandler(self.__interactor_factory, self.__renderer),
            "DeletePlatformHandler": DeletePlatformHandler(self.__interactor_factory, self.__renderer),
            "EditHardwareHandler": EditHardwareHandler(self.__interactor_factory, self.__renderer),
            "UpdateHardwareHandler": UpdateHardwareHandler(self.__interactor_factory, self.__renderer),
            "DeleteHardwareHandler": DeleteHardwareHandler(self.__interactor_factory, self.__renderer),
            "GetGenresHandler": GetGenresHandler(self.__interactor_factory, self.__renderer),
            "AddGenreHandler": AddGenreHandler(self.__interactor_factory, self.__renderer),
            "EditGenreHandler": EditGenreHandler(self.__interactor_factory, self.__renderer),
            "UpdateGenreHandler": UpdateGenreHandler(self.__interactor_factory, self.__renderer),
            "DeleteGenreHandler": DeleteGenreHandler(self.__interactor_factory, self.__renderer),
            "AllGamesHandler": AllGamesHandler(self.__interactor_factory, self.__renderer)
        }

    def create(self, handler_type):

        if handler_type in self.__handlers:
            return self.__handlers[handler_type]

        raise UnrecognisedHandlerException
