from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException

class Handler(object):

    def __init__(self, interactor_factory, renderer):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__session = None

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

    def set_if_null(self, variable, value):
        if variable is None:
            return value
        return variable

    def check_session(self):
        if self.session is None:
            raise SessionNotSetException
