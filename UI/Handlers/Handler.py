# Copyright (c) 2015 David Wilson
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

import cherrypy
from UI.Handlers.Exceptions.CookiesNotSetException import CookiesNotSetException
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException

class Handler(object):

    def __init__(self, interactor_factory, renderer):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__session = None
        self.__cookies = None

    @property
    def interactor_factory(self):
        return self.__interactor_factory

    @property
    def renderer(self):
        return self.__renderer

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, val):
        self.__session =  val

    @property
    def cookies(self):
        return self.__cookies

    @cookies.setter
    def cookies(self, val):
        self.__cookies = val

    def set_if_null(self, variable, value):
        if variable is None:
            return value
        return variable

    def check_session(self):
        if self.session is None:
            raise SessionNotSetException

    def check_cookies(self):
        if self.cookies is None:
            raise CookiesNotSetException

    def logged_in(self):
        return self.session.get_value("user_id") != ""

    def redirect_if_not_logged_in(self):
        if not self.logged_in():
            raise cherrypy.HTTPRedirect("/login")

    def validate_params(self, params, fields):
        invalid_fields = sum(map(lambda x: x not in params or str(params[x]).strip() == "" or params[x] == None, fields))
        return invalid_fields == 0

    def renew_cookies(self):
        if self.__cookies is None:
            raise ValueError("Cookies object not set")
        self.__cookies.renew_cookie("user_id")
        self.__cookies.renew_cookie("session_status")
