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

    @cherrypy.expose
    def index(self, **kwargs):
        return self.__get_page("IndexHandler", kwargs)

    @cherrypy.expose
    def addgame(self, **kwargs):
        return self.__get_page("AddGameHandler", kwargs)

    @cherrypy.expose
    def savegame(self, **kwargs):
        return self.__get_page("SaveGameHandler", kwargs)

    @cherrypy.expose()
    def addhardware(self, **kwargs):
        return self.__get_page("AddHardwareHandler", kwargs)

    @cherrypy.expose
    def platforms(self, **kwargs):
        return self.__get_page("PlatformsHandler", kwargs)

    @cherrypy.expose
    def addplatform(self, **kwargs):
        return self.__get_page("AddPlatformHandler", kwargs)

    @cherrypy.expose
    def editgame(self, **kwargs):
        return self.__get_page("EditGameHandler", kwargs)

    @cherrypy.expose
    def updategame(self, **kwargs):
        return self.__get_page("UpdateGameHandler", kwargs)

    @cherrypy.expose
    def deletegame(self, **kwargs):
        return self.__get_page("DeleteGameHandler", kwargs)

    @cherrypy.expose
    def editplatform(self, **kwargs):
        return self.__get_page("EditPlatformHandler", kwargs)

    @cherrypy.expose
    def deleteplatform(self, **kwargs):
        return self.__get_page("DeletePlatformHandler", kwargs)

    @cherrypy.expose
    def updateplatform(self, **kwargs):
        return self.__get_page("UpdatePlatformHandler", kwargs)

    @cherrypy.expose
    def savehardware(self, **kwargs):
        return self.__get_page("SaveHardwareHandler", kwargs)

    @cherrypy.expose
    def edithardware(self, **kwargs):
        return self.__get_page("EditHardwareHandler", kwargs)

    @cherrypy.expose
    def updatehardware(self, **kwargs):
        return self.__get_page("UpdateHardwareHandler", kwargs)

    @cherrypy.expose
    def deletehardware(self, **kwargs):
        return self.__get_page("DeleteHardwareHandler", kwargs)

    @cherrypy.expose
    def allgames(self, **kwargs):
        return self.__get_page("AllGamesHandler", kwargs)

    @cherrypy.expose
    def search(self, **kwargs):
        return self.__get_page("SearchHandler", kwargs)

    def __get_page(self, handler_name, args):
        handler = self.handler_factory.create(handler_name)
        return handler.get_page(args)