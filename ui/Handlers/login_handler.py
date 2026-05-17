"""Handler for the login page."""
import cherrypy
from ui.Handlers.handler import Handler


class LoginHandler(Handler):
    """Handler for the login page."""

    def get_page(self, _args):
        """Returns the login page."""
        self.check_session()
        if self.logged_in():
            raise cherrypy.HTTPRedirect("/")
        return self.renderer.render("login.html")
