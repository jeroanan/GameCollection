from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.AllHardwareHandler import AllHardwareHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.LoginHandler import LoginHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.SearchHandler import SearchHandler
from UI.Handlers.SignupHandler import SignupHandler
from UI.Handlers.SigninHandler import SigninHandler
from UI.Handlers.SortGamesHandler import SortGamesHandler
from UI.Handlers.SortHardwareHandler import SortHardwareHandler
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Handlers.Session.Session import Session
from UI.Tests.Handlers.TestEditPlatformHandler import EditPlatformHandler



class HandlerFactory(object):

    def __init__(self, interactor_factory, renderer, config):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__config = config

        self.__handlers = {
            "index": IndexHandler,
            "savegame": SaveGameHandler,
            "addgame": AddGameHandler,
            "addhardware": AddHardwareHandler,
            "platforms": PlatformsHandler,
            "addplatform": AddPlatformHandler,
            "editgame": EditGameHandler,
            "updategame": UpdateGameHandler,
            "deletegame": DeleteGameHandler,
            "savehardware": SaveHardwareHandler,
            "editplatform": EditPlatformHandler,
            "updateplatform": UpdatePlatformHandler,
            "deleteplatform": DeletePlatformHandler,
            "edithardware": EditHardwareHandler,
            "updatehardware": UpdateHardwareHandler,
            "deletehardware": DeleteHardwareHandler,
            "allgames": AllGamesHandler,
            "search": SearchHandler,
            "allhardware": AllHardwareHandler,
            "sortgames": SortGamesHandler,
            "sorthardware": SortHardwareHandler,
            "login": LoginHandler,
            "signup": SignupHandler,
            "signin": SigninHandler
        }

    def create(self, handler_type):
        
        if handler_type == "index":
            return  IndexHandler(self.__interactor_factory, self.__renderer, self.__config)

        if handler_type in self.__handlers:
            handler = self.__handlers[handler_type](self.__interactor_factory, self.__renderer)
            handler.session = Session()
            return handler

        raise UnrecognisedHandlerException
