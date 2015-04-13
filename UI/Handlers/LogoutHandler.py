import cherrypy
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class LogoutHandler(AuthenticatedHandler):
    
    def get_page(self, args):
        super().get_page(args)
        self.check_cookies()
        self.cookies.clear_cookie("session_status")
        self.cookies.clear_cookie("user_id")
        self.session.expire()
        raise cherrypy.HTTPRedirect("/")
