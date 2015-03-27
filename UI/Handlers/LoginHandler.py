from UI.Handlers.Handler import Handler


class LoginHandler(Handler):
    def get_page(self, args):
        return self.renderer.render("login.html")
