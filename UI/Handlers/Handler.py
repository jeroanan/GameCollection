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
        invalid_fields = sum(map(lambda x: x not in params or params[x] == "", fields))
        return invalid_fields == 0
