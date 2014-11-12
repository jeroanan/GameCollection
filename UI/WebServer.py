import cherrypy
from Game import Game
from Platform import Platform
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
        cherrypy.quickstart(WebServer(interactor_factory))

    @cherrypy.expose
    def index(self):
        handler = self.handler_factory.create("IndexHandler")
        return handler.get_page()

    @cherrypy.expose
    def addgame(self):
        return self.renderer.render("addgame.html", title="Add Game")

    @cherrypy.expose
    def savegame(self, title, numcopies, numboxed, nummanuals, platform=None):
        interactor = self.__interactor_factory.create("AddGameInteractor")
        game = Game()
        game.title = title
        game.num_copies = numcopies
        game.num_boxed = numboxed
        game.num_manuals = nummanuals
        game.platform = platform
        interactor.execute(game)
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose()
    def addhardware(self):
        return self.renderer.render("addhardware.html", title="Add Hardware")

    @cherrypy.expose
    def platforms(self):
        interactor = self.__interactor_factory.create("GetPlatformsInteractor")
        platforms = interactor.execute()
        return self.renderer.render("platforms.html", title="Manage Platforms", platforms=platforms)

    @cherrypy.expose
    def addplatform(self, name, description):
        interactor = self.__interactor_factory.create("AddPlatformInteractor")
        platform = Platform()
        platform.name = name
        platform.description = description
        interactor.execute(platform)
        raise cherrypy.HTTPRedirect("/platforms")
