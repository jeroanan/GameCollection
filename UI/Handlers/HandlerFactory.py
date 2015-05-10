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

        def string_to_handler():
            ht = self.__handlers[handler_type]
            module = __import__("UI.Handlers." + ht, fromlist=ht)
            class_ = getattr(module, ht)
            return class_(self.__interactor_factory, self.__renderer)

        handler = None

        if handler_type == "index":
            handler = IndexHandler(self.__interactor_factory, self.__renderer, self.__config)
        elif handler_type in self.__handlers:
            handler = string_to_handler()
        else:
            raise UnrecognisedHandlerException

        handler.session = Session()
        handler.cookies = Cookies()
        return handler

    
