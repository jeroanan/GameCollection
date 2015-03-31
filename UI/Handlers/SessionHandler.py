from UI.Handlers.Handler import Handler

class SessionHandler(Handler):
    
    def __init__(self, interactor_factory, renderer, session):
        super().__init__(interactor_factory, renderer)
