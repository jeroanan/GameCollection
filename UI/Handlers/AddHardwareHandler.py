from UI.Handlers.Handler import Handler


class AddHardwareHandler(Handler):

    def get_page(self):
        return self.renderer.render("addhardware.html", title="Add Hardware")