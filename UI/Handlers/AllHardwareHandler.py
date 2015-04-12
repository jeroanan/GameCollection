from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AllHardwareHandler(AuthenticatedHandler):

    """The All Hardware page
    Shows a list of all the hardware that the current user has in their collection.
    param args: Seems not to be currently used. TODO: why not?
    returns: The rendered all hardware page
    """
    def get_page(self, args):
        super().get_page(args)
        interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = interactor.execute(sort_field="name", sort_direction="asc", user_id=self.session.get_value("user_id"))
        return self.renderer.render("allhardware.html", hardware=hardware, title="All Hardware",
                                    hw_sort_field="name", hw_sort_dir="asc")
