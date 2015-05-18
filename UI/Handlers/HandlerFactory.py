# copyright (c) David Wilson 2015
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

import json

from UI.Cookies.Cookies import Cookies
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.Session.Session import Session

class HandlerFactory(object):

    def __init__(self, interactor_factory, renderer, config):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__config = config
        self.__handlers = self.__load_handlers()

    def __load_handlers(self):
        with open("UI/Handlers/handlers.json") as f:
            return json.load(f)["handlers"][0]        

    def create(self, handler_type):
        handler = None

        def renew_cookies():
            if handler is None:
                raise ValueError("handler not set")
            handler.renew_cookies()

        def string_to_handler():
            ht = self.__handlers[handler_type]
            module = __import__("UI.Handlers." + ht, fromlist=ht)
            class_ = getattr(module, ht)
            return class_(self.__interactor_factory, self.__renderer)

        if handler_type == "index":
            handler = IndexHandler(self.__interactor_factory, self.__renderer, self.__config)
        elif handler_type in self.__handlers:
            handler = string_to_handler()
        else:
            raise UnrecognisedHandlerException

        handler.session = Session()
        handler.cookies = Cookies()
        renew_cookies()
        return handler

    
