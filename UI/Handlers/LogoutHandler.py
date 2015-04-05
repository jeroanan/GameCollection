import cherrypy
from UI.Handlers.Handler import Handler


class LogoutHandler(Handler):
    
    def get_page(self, args):
        self.check_session()
        self.check_cookies()
        self.cookies.clear_cookie("session_status")
        self.cookies.clear_cookie("user_id")
        self.session.expire()
        raise cherrypy.HTTPRedirect("/")
