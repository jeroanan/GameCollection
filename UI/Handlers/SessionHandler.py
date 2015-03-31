from UI.Handlers.Handler import Handler

class SessionHandler(Handler):
    
    def __init__(self, interactor_factory, renderer):
        super().__init__(interactor_factory, renderer)
        self.__session = None

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, val):
        self.__session = val
