"""Web server for Icarus UI"""
# This file is part of Icarus.

# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

import logging

import cherrypy

from ui.handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException

from ui.handlers.handler_factory import HandlerFactory
from ui.template_renderer import TemplateRenderer


class WebServer:
    """Icarus Web Server"""
    def __init__(self, interactor_factory=None, renderer=None, config=None, logger=None):
        # TODO: we should just use dependency injection here
        self.__logger = logger
        self.__renderer = renderer
        self.__set_defaults()
        self.__handler_factory = HandlerFactory(interactor_factory, self.__renderer, config)

    def __set_defaults(self):
        if self.__renderer is None:
            self.__renderer = TemplateRenderer()
        if self.__logger is None:
            self.__logger = logging.basicConfig()

    @property
    def renderer(self):
        """Return the renderer"""
        return self.__renderer

    @property
    def handler_factory(self):
        """Return the handler factory"""
        return self.__handler_factory

    @handler_factory.setter
    def handler_factory(self, value):
        self.__handler_factory = value

    def start(self, interactor_factory, config, logger):
        """Start the web server"""
        cherrypy.quickstart(
            WebServer(interactor_factory=interactor_factory, config=config,logger=logger),
            '/',
            'ui/app.conf')

    @cherrypy.expose()
    def default(self, *args, **kwargs):
        """The default handler for all requests"""
        if not args:
            return self.__get_page("index", kwargs)

        try:
            return self.__get_page(args[0], kwargs)
        except UnrecognisedHandlerException:
            raise cherrypy.NotFound

    def __get_page(self, handler_name, args):
        handler = self.handler_factory.create(handler_name)
        return handler.get_page(args)
