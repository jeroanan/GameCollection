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

from typing import Any

import cherrypy

from interactors.interactor_factory import InteractorFactory
from ui.Cookies.cookies import Cookies
from ui.handlers.Exceptions.CookiesNotSetException import CookiesNotSetException
from ui.handlers.Exceptions.SessionNotSetException import SessionNotSetException
from ui.handlers.Session.Session import Session
from ui.template_renderer import TemplateRenderer

class Handler:
    """Base class for all handlers. Provides common functionality and properties."""

    def __init__(self, interactor_factory: InteractorFactory, renderer: TemplateRenderer) -> None:
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__session: Session | None = None
        self.__cookies: Cookies | None = None

    @property
    def interactor_factory(self) -> InteractorFactory:
        """Returns the interactor factory."""
        return self.__interactor_factory

    @property
    def renderer(self) -> TemplateRenderer:
        """Returns the renderer."""
        return self.__renderer

    @property
    def session(self) -> Session | None:
        """Returns the session."""
        return self.__session

    @session.setter
    def session(self, val: Session) -> None:
        self.__session =  val

    @property
    def cookies(self) -> Cookies | None:
        """Returns the cookies."""
        return self.__cookies

    @cookies.setter
    def cookies(self, val: Cookies) -> None:
        self.__cookies = val

    def set_if_null(self, variable: Any, value: Any) -> Any:
        """Returns the variable if it is not None, otherwise returns the value."""
        if variable is None:
            return value
        return variable

    def check_session(self) -> None:
        """Checks if the session is set, if not raises an exception."""
        if self.session is None:
            raise SessionNotSetException

    def check_cookies(self) -> None:
        """Checks if the cookies are set, if not raises an exception."""
        if self.cookies is None:
            raise CookiesNotSetException

    def logged_in(self) -> bool:
        """Returns True if the user is logged in, False otherwise."""
        return self.session.get_value("user_id") != ""

    def redirect_if_not_logged_in(self) -> None:
        """Redirects to the login page if the user is not logged in."""
        if not self.logged_in():
            raise cherrypy.HTTPRedirect("/login")

    def validate_params(self, params: dict[str, str], fields: list[str]) -> bool:
        """Validates that the required fields are present in the params and are not empty."""
        invalid_fields = sum(map(
            lambda x: x not in params or str(params[x]).strip() == "" or params[x] is None, fields))
        return invalid_fields == 0

    def renew_cookies(self) -> None:
        """Renews the cookies for the user."""
        if self.__cookies is None:
            raise ValueError("Cookies object not set")
        self.__cookies.renew_cookie("user_id")
        self.__cookies.renew_cookie("session_status")
