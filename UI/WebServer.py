import os

import cherrypy
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException

from UI.Handlers.HandlerFactory import HandlerFactory
from UI.TemplateRenderer import TemplateRenderer


class WebServer(object):
    def __init__(self, interactor_factory=None, renderer=None, config=None):
        self.__renderer = renderer
        if renderer is None:
            self.__renderer = TemplateRenderer()
        self.__handler_factory = HandlerFactory(interactor_factory, self.__renderer, config)

    @property
    def renderer(self):
        return self.__renderer

    @property
    def handler_factory(self):
        return self.__handler_factory

    @handler_factory.setter
    def handler_factory(self, value):
        self.__handler_factory = value

    def start(self, interactor_factory, config):
        cherrypy.quickstart(WebServer(interactor_factory=interactor_factory, config=config), '/', 'UI/app.conf')

    @cherrypy.expose()
    def default(self, *args, **kwargs):
        if args == ():
            return self.__get_page("index", kwargs)
        else:
            try:
                return self.__get_page(args[0], kwargs)
            except UnrecognisedHandlerException:
                raise cherrypy.NotFound

    def __get_page(self, handler_name, args):
        handler = self.handler_factory.create(handler_name)
        return handler.get_page(args)
