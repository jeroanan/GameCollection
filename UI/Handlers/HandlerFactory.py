from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.IndexHandler import IndexHandler


class HandlerFactory(object):

    def __init__(self, interactor_factory, renderer):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer

    def create(self, handler_type):
        if handler_type == "IndexHandler":
            return IndexHandler(self.__interactor_factory, self.__renderer)
        raise UnrecognisedHandlerException
