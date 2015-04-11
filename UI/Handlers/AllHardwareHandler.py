from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AllHardwareHandler(AuthenticatedHandler):

    def get_page(self, args):
        super().get_page(args)
        interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = interactor.execute(sort_field="name", sort_direction="asc")
        return self.renderer.render("allhardware.html", hardware=hardware, title="All Hardware",
                                    hw_sort_field="name", hw_sort_dir="asc")
