from UI.Handlers.Handler import Handler


class AuthenticatedHandler(Handler):
    
    def get_page(self, params):
        self.check_session()
        self.redirect_if_not_logged_in()
