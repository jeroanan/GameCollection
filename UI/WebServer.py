import cherrypy
from Game import Game
from UI.TemplateRenderer import TemplateRenderer


class WebServer(object):

    def __init__(self, interactor_factory=None, renderer=None):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        if renderer is None:
            self.__renderer = TemplateRenderer()

    @property
    def renderer(self):
        return self.__renderer

    def start(self, interactor_factory):
        cherrypy.quickstart(WebServer(interactor_factory))

    @cherrypy.expose
    def index(self):
        interactor = self.__interactor_factory.create("GetGamesInteractor")
        games = interactor.execute()
        return self.renderer.render("index.html", games=games, title="Games Collection")

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
        interactor.execute(name, description)
        raise cherrypy.HTTPRedirect("/platforms")
