import cherrypy
from UI.Handlers.Handler import Handler


class LoginHandler(Handler):
    def get_page(self, args):
        self.check_session()
        if self.logged_in():
            raise cherrypy.HTTPRedirect("/")        
        return self.renderer.render("login.html")

