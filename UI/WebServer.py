import os
import cherrypy
from UI.Handlers.AddPlatformHandler.AddPlatformHandlerParams import AddPlatformHandlerParams
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.Handlers.IndexHandler.IndexHandlerParams import IndexHandlerParams
from UI.Handlers.SaveGameHandler.SaveGameHandlerParams import SaveGameHandlerParams
from UI.Handlers.SaveHardwareHandler.SaveHardwareHandlerParams import SaveHardwareHandlerParams
from UI.Handlers.UpdateGameHandler.UpdateGameHandlerParams import UpdateGameHandlerParams
from UI.Handlers.UpdatePlatformHandler.UpdatePlatformHandlerParams import UpdatePlatformHandlerParams
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
    def index(self, gamesort=None, gamesortdir=None, hardwaresort=None, hardwaresortdir=None):
        handler = self.handler_factory.create("IndexHandler")

        params = IndexHandlerParams()
        params.game_sort = gamesort
        params.game_sort_direction = gamesortdir
        params.hardware_sort = hardwaresort
        params.hardware_sort_direction = hardwaresortdir
        return handler.get_page(params)

    @cherrypy.expose
    def addgame(self):
        return self.__get_page_for_handler("AddGameHandler")

    @cherrypy.expose
    def savegame(self, title, numcopies, numboxed, nummanuals, platform, notes):
        handler = self.__handler_factory.create("SaveGameHandler")

        params = SaveGameHandlerParams()
        params.title = title
        params.num_copies = numcopies
        params.num_boxed = numboxed
        params.num_manuals = nummanuals
        params.platform = platform
        params.notes = notes
        return handler.get_page(params=params)

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
        params = AddPlatformHandlerParams()
        params.name = name
        params.description = description
        return handler.get_page(platform=params)

    @cherrypy.expose
    def editgame(self, gameid):
        handler = self.__handler_factory.create("EditGameHandler")
        return handler.get_page(game_id=gameid)

    @cherrypy.expose
    def updategame(self, id, title, platform, numcopies, numboxed, nummanuals, notes):
        p = UpdateGameHandlerParams()
        p.id = id
        p.title = title
        p.platform = platform
        p.num_copies = numcopies
        p.num_boxed = numboxed
        p.num_manuals = nummanuals
        p.notes = notes

        handler = self.__handler_factory.create("UpdateGameHandler")
        return handler.get_page(params=p)

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
        params = UpdatePlatformHandlerParams()
        params.id = id
        params.name = name
        params.description = description
        handler = self.__handler_factory.create("UpdatePlatformHandler")
        handler.get_page(params=params)

    @cherrypy.expose
    def savehardware(self, name, platform, numowned, numboxed, notes):
        params = SaveHardwareHandlerParams()
        params.name = name
        params.platform = platform
        params.num_owned = numowned
        params.num_boxed = numboxed
        params.notes = notes

        handler = self.__handler_factory.create("SaveHardwareHandler")
        return handler.get_page(params=params)

    @cherrypy.expose
    def edithardware(self, hardwareid):
        handler = self.__handler_factory.create("EditHardwareHandler")
        return handler.get_page(hardwareid)

    @cherrypy.expose
    def updatehardware(self, id, name, platform, numcopies, numboxed, notes):
        handler = self.__handler_factory.create("UpdateHardwareHandler")
        handler.get_page(id=id, name=name, platform=platform, numowned=numcopies, numboxed=numboxed, notes=notes)

    @cherrypy.expose
    def deletehardware(self, hardwareid):
        handler = self.__handler_factory.create("DeleteHardwareHandler")
        handler.get_page(hardware_id=hardwareid)

    @cherrypy.expose
    def allgames(self, gamesort=None, gamesortdir=None, platform=None):
        handler = self.__handler_factory.create("AllGamesHandler")
        return handler.get_page(sort_field=gamesort, sort_direction=gamesortdir, platform=platform)

    @cherrypy.expose
    def search(self, searchterm, gamesort=None, gamesortdir=None):
        handler = self.__handler_factory.create("SearchHandler")
        return handler.get_page(search_term=searchterm, sort_field=gamesort, sort_dir=gamesortdir)