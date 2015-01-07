from UI.Handlers.Handler import Handler


class AllHardwareHandler(Handler):
    def get_page(self, args):
        interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = interactor.execute(sort_field="name", sort_direction="asc")
        return self.renderer.render("allhardware.html", hardware=hardware, title="All Hardware")
