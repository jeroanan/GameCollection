import os

import cherrypy

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
        conf = {
            '/': {
                'tools.sessions.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd()),
                'tools.gzip.on': True
            },
            '/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './UI/markup/',
                'tools.gzip.on': True
            }
        }
        cherrypy.quickstart(WebServer(interactor_factory=interactor_factory, config=config), '/', conf)

    @cherrypy.expose()
    def default(self, *args, **kwargs):
        if args == ():
            return self.__get_page("IndexHandler", kwargs)
        elif args[0] == "addgame":
            return self.__get_page("AddGameHandler", kwargs)
        elif args[0] == "savegame":
            return self.__get_page("SaveGameHandler", kwargs)
        elif args[0] == "addhardware":
            return self.__get_page("AddHardwareHandler", kwargs)
        elif args[0] == "platforms":
            return self.__get_page("PlatformsHandler", kwargs)
        elif args[0] == "addplatform":
            return self.__get_page("AddPlatformHandler", kwargs)
        elif args[0] == "editgame":
            return self.__get_page("EditGameHandler", kwargs)
        elif args[0] == "updategame":
            return self.__get_page("UpdateGameHandler", kwargs)
        elif args[0] == "deletegame":
            return self.__get_page("DeleteGameHandler", kwargs)
        elif args[0] == "editplatform":
            return self.__get_page("EditPlatformHandler", kwargs)
        elif args[0] == "deleteplatform":
            return self.__get_page("DeletePlatformHandler", kwargs)
        elif args[0] == "updateplatform":
            return self.__get_page("UpdatePlatformHandler", kwargs)
        elif args[0] == "savehardware":
            return self.__get_page("SaveHardwareHandler", kwargs)
        elif args[0] == "edithardware":
            return self.__get_page("EditHardwareHandler", kwargs)
        elif args[0] == "updatehardware":
            return self.__get_page("UpdateHardwareHandler", kwargs)
        elif args[0] == "deletehardware":
            return self.__get_page("DeleteHardwareHandler", kwargs)
        elif args[0] == "allgames":
            return self.__get_page("AllGamesHandler", kwargs)
        elif args[0] == "search":
            return  self.__get_page("SearchHandler", kwargs)

    def __get_page(self, handler_name, args):
        handler = self.handler_factory.create(handler_name)
        return handler.get_page(args)