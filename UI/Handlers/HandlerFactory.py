from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.EditHandler import EditHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Tests.Handlers.TestEditPlatformHandler import EditPlatformHandler


class HandlerFactory(object):

    def __init__(self, interactor_factory, renderer):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer

    def create(self, handler_type):
        if handler_type == "IndexHandler":
            return IndexHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "SaveGameHandler":
            return SaveGameHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "AddGameHandler":
            return AddGameHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "AddHardwareHandler":
            return AddHardwareHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "PlatformsHandler":
            return PlatformsHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "AddPlatformHandler":
            return AddPlatformHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "EditGameHandler":
            return EditHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "UpdateGameHandler":
            return UpdateGameHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "DeleteGameHandler":
            return DeleteGameHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "SaveHardwareHandler":
            return SaveHardwareHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "EditPlatformHandler":
            return EditPlatformHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "UpdatePlatformHandler":
            return UpdatePlatformHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "DeletePlatformHandler":
            return DeletePlatformHandler(self.__interactor_factory, self.__renderer)
        if handler_type == "EditHardwareHandler":
            return EditHardwareHandler(self.__interactor_factory, self.__renderer)

        raise UnrecognisedHandlerException
