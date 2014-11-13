from UI.Handlers.Handler import Handler


class EditHandler(Handler):

    def get_page(self, game_id):
        return self.renderer.render("edit.html")