import os

import cherrypy

from UI.Handlers.HandlerFactory import HandlerFactory
from UI.TemplateRenderer import TemplateRenderer


class WebServer(object):

    def __init__(self, interactor_factory=None, renderer=None, config=None):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        if renderer is None:
            self.__renderer = TemplateRenderer()
        self.__handler_factory = HandlerFactory(interactor_factory, self.__renderer, config)
        self.__config = config

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
        handler = self.handler_factory.create("IndexHandler")
        return handler.get_page(kwargs)

    @cherrypy.expose
    def addgame(self):
        return self.__get_page_for_handler("AddGameHandler")

    @cherrypy.expose
    def savegame(self, **kwargs):
        handler = self.__handler_factory.create("SaveGameHandler")
        return handler.get_page(params=kwargs)

    @cherrypy.expose()
    def addhardware(self):
        return self.__get_page_for_handler("AddHardwareHandler")

    @cherrypy.expose
    def platforms(self):
        return self.__get_page_for_handler("PlatformsHandler")

    def __get_page_for_handler(self, type_string):
        handler = self.__handler_factory.create(type_string)
        return handler.get_page()

    @cherrypy.expose
    def addplatform(self, **kwargs):
        handler = self.__handler_factory.create("AddPlatformHandler")
        return handler.get_page(platform=kwargs)

    @cherrypy.expose
    def editgame(self, gameid):
        handler = self.__handler_factory.create("EditGameHandler")
        return handler.get_page(game_id=gameid)

    @cherrypy.expose
    def updategame(self, **kwargs):
        handler = self.__handler_factory.create("UpdateGameHandler")
        return handler.get_page(params=kwargs)

    @cherrypy.expose
    def deletegame(self, gameid):
        handler = self.__handler_factory.create("DeleteGameHandler")
        return handler.get_page(gameid)

    @cherrypy.expose
    def editplatform(self, platformid):
        handler = self.__handler_factory.create("EditPlatformHandler")
        return handler.get_page(platformid)

    @cherrypy.expose
    def deleteplatform(self, platformid):
        handler = self.__handler_factory.create("DeletePlatformHandler")
        handler.get_page(platformid)

    @cherrypy.expose
    def updateplatform(self, **kwargs):
        handler = self.__handler_factory.create("UpdatePlatformHandler")
        handler.get_page(params=kwargs)

    @cherrypy.expose
    def savehardware(self, **kwargs):
        handler = self.__handler_factory.create("SaveHardwareHandler")
        return handler.get_page(params=kwargs)

    @cherrypy.expose
    def edithardware(self, hardwareid):
        handler = self.__handler_factory.create("EditHardwareHandler")
        return handler.get_page(hardwareid)

    @cherrypy.expose
    def updatehardware(self, **kwargs):
        handler = self.__handler_factory.create("UpdateHardwareHandler")
        handler.get_page(params=kwargs)

    @cherrypy.expose
    def deletehardware(self, hardwareid):
        handler = self.__handler_factory.create("DeleteHardwareHandler")
        handler.get_page(hardware_id=hardwareid)

    @cherrypy.expose
    def allgames(self, **kwargs):
        handler = self.__handler_factory.create("AllGamesHandler")
        return handler.get_page(params=kwargs)

    @cherrypy.expose
    def search(self, **kwargs):
        handler = self.__handler_factory.create("SearchHandler")
        return handler.get_page(params=kwargs)