"""Base class for all handlers. Provides common functionality and properties."""
# Copyright (c) 2015, 2026 David Wilson
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

class Handler:
    """Base class for all handlers. Provides common functionality and properties."""

    def __init__(self, interactor_factory, renderer):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__session = None
        self.__cookies = None

    @property
    def interactor_factory(self):
        """Returns the interactor factory."""
        return self.__interactor_factory

    @property
    def renderer(self):
        """Returns the renderer."""
        return self.__renderer

    @property
    def session(self):
        """Returns the session."""
        return self.__session

    @session.setter
    def session(self, val):
        self.__session =  val

    @property
    def cookies(self):
        """Returns the cookies."""
        return self.__cookies

    @cookies.setter
    def cookies(self, val):
        self.__cookies = val

    def set_if_null(self, variable, value):
        """Returns the variable if it is not None, otherwise returns the value."""
        if variable is None:
            return value
        return variable

    def check_session(self):
        """Checks if the session is set, if not raises an exception."""
        if self.session is None:
            raise SessionNotSetException

    def check_cookies(self):
        """Checks if the cookies are set, if not raises an exception."""
        if self.cookies is None:
            raise CookiesNotSetException

    def logged_in(self):
        """Returns True if the user is logged in, False otherwise."""
        return self.session.get_value("user_id") != ""

    def redirect_if_not_logged_in(self):
        """Redirects to the login page if the user is not logged in."""
        if not self.logged_in():
            raise cherrypy.HTTPRedirect("/login")

    def validate_params(self, params, fields):
        """Validates that the required fields are present in the params and are not empty."""
        invalid_fields = sum(map(
            lambda x: x not in params or str(params[x]).strip() == "" or params[x] is None, fields))
        return invalid_fields == 0

    def renew_cookies(self):
        """Renews the cookies for the user."""
        if self.__cookies is None:
            raise ValueError("Cookies object not set")
        self.__cookies.renew_cookie("user_id")
        self.__cookies.renew_cookie("session_status")
