import os
import cherrypy
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.TemplateRenderer import TemplateRenderer


class WebServer(object):

    def __init__(self, interactor_factory=None, renderer=None):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        if renderer is None:
            self.__renderer = TemplateRenderer()
        self.__handler_factory = HandlerFactory(interactor_factory, self.__renderer)

    @property
    def renderer(self):
        return self.__renderer

    @property
    def handler_factory(self):
        return self.__handler_factory

    @handler_factory.setter
    def handler_factory(self, value):
        self.__handler_factory = value

    def start(self, interactor_factory):
        conf = {
         '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './UI/markup/'
         }
        }
        cherrypy.quickstart(WebServer(interactor_factory), '/', conf)

    @cherrypy.expose
    def index(self):
        return self.__get_page_for_handler("IndexHandler")

    @cherrypy.expose
    def addgame(self):
        return self.__get_page_for_handler("AddGameHandler")

    @cherrypy.expose
    def savegame(self, title, numcopies, numboxed, nummanuals, platform=None):
        handler = self.__handler_factory.create("SaveGameHandler")
        return handler.get_page(title, numcopies, numboxed, nummanuals, platform)

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
    def addplatform(self, name, description):
        handler = self.__handler_factory.create("AddPlatformHandler")
        return handler.get_page(name, description)

    @cherrypy.expose
    def editgame(self, gameid):
        handler = self.__handler_factory.create("EditGameHandler")
        return handler.get_page(gameid)

    @cherrypy.expose
    def updategame(self, id, title, platform, numcopies, numboxed, nummanuals):
        handler = self.__handler_factory.create("UpdateGameHandler")
        return handler.get_page(id=id, title=title, platform=platform, numcopies=numcopies, numboxed=numboxed,
                                nummanuals=nummanuals)

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
    def updateplatform(self, id, name, description):
        handler = self.__handler_factory.create("UpdatePlatformHandler")
        handler.get_page(id, name, description)

    @cherrypy.expose
    def savehardware(self, name, platform, numowned, numboxed):
        handler = self.__handler_factory.create("SaveHardwareHandler")
        return handler.get_page(name=name, platform=platform, numowned=numowned, numboxed=numboxed)

    @cherrypy.expose
    def edithardware(self, hardwareid):
        handler = self.__handler_factory.create("EditHardwareHandler")
        return handler.get_page(hardwareid)
