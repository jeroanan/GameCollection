from UI.Handlers.Handler import Handler


class AddGameHandler(Handler):

    def get_page(self):
        return self.renderer.render("addgame.html", title="Add Game")
