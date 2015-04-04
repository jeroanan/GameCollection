import json

from UI.Cookies.Cookies import Cookies
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.Session.Session import Session

class HandlerFactory(object):

    def __init__(self, interactor_factory, renderer, config):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__config = config
        self.__handlers = self.__load_handlers()

    def __load_handlers(self):
        with open("UI/Handlers/handlers.json") as f:
            return json.load(f)["handlers"][0]        

    def create(self, handler_type):
        if handler_type == "index":
            return  IndexHandler(self.__interactor_factory, self.__renderer, self.__config)        

        if handler_type in self.__handlers:
            handler = self.__string_to_handler(self.__handlers[handler_type])
            handler.session = Session()
            handler.cookies = Cookies()
            return handler

        raise UnrecognisedHandlerException

    def __string_to_handler(self, handler_type):
        module = __import__("UI.Handlers." + handler_type, fromlist=handler_type)
        class_ = getattr(module, handler_type)
        return class_(self.__interactor_factory, self.__renderer)
