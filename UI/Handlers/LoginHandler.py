import cherrypy
from UI.Handlers.Handler import Handler


class LoginHandler(Handler):
    def get_page(self, args):
        self.check_session()
        if self.__logged_in():
            raise cherrypy.HTTPRedirect("/")        
        return self.renderer.render("login.html")

    def __logged_in(self):
        return self.session.get_value("user_id") != ""
