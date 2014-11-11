import cherrypy
from jinja2 import Environment, PackageLoader
from GamesGateway import GamesGateway
from GamesInteractor import GamesInteractor


class WebServer(object):

    def start(self):
        cherrypy.quickstart(WebServer())

    def index(self):
        template = self.__get_template("index.html")
        interactor = GamesInteractor()
        interactor.games_gateway = GamesGateway()
        return template.render(games=interactor.get_my_games())

    def addgame(self):
        template = self.__get_template("addgame.html")
        return template.render()

    def platforms(self):
        template = self.__get_template("platforms.html")
        return template.render()

    def __get_template(self, template):
        env = Environment(loader=PackageLoader("WebServer", "markup"))
        return env.get_template(template)

    index.exposed = True
    addgame.exposed = True
    platforms.exposed = True

if __name__ == "__main__":
    app = WebServer()
    app.start()