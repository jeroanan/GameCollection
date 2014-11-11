import cherrypy
from jinja2 import Environment, PackageLoader
from GamesGateway import GamesGateway
from GetGamesInteractor import GetGamesInteractor


class WebServer(object):

    def start(self):
        cherrypy.quickstart(WebServer())

    @cherrypy.expose
    def index(self):
        interactor = GetGamesInteractor()
        interactor.games_gateway = GamesGateway()
        return self.__render_template("index.html", games=interactor.execute(), title="Games Collection")

    @cherrypy.expose
    def addgame(self):
        return self.__render_template("addgame.html", title="Add Game")

    @cherrypy.expose
    def savegame(self, **kwargs):
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose()
    def addhardware(self):
        return self.__render_template("addhardware.html", title="Add Hardware")

    @cherrypy.expose
    def platforms(self):
        return self.__render_template("platforms.html", title="Manage Platforms")

    def __render_template(self, template, **args):
        template = self.__get_template(template)
        return template.render(args)

    def __get_template(self, template):
        env = Environment(loader=PackageLoader("WebServer", "markup"))
        return env.get_template(template)

if __name__ == "__main__":
    app = WebServer()
    app.start()