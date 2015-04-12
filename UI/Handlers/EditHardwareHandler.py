from Persistence.Exceptions.HardwareNotFoundException import HardwareNotFoundException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class EditHardwareHandler(AuthenticatedHandler):

    """The Edit Hardware page.
    param args: A dictionary containing the keys:
                + 'hardwareid' -- the uuid of the hardware item to be edited
    return: The rendered Edit Hardware page. 
            If the hardware is not found then a "Hardware Not Found" message is displayed to the user.
    """
    def get_page(self, args):
        super().get_page(args)
        get_hardware_details_interactor = self.interactor_factory.create("GetHardwareDetailsInteractor")
        get_platforms_interactor = self.interactor_factory.create("GetPlatformsInteractor")

        hardware = []
        platforms = []
        page_title = "Edit Hardware"
        hardware_found = True

        try:
            hardware = get_hardware_details_interactor.execute(args.get("hardwareid", ""), 
                                                               self.session.get_value("user_id"))
            platforms = get_platforms_interactor.execute()
        except HardwareNotFoundException:
            page_title = "Hardware Not Found"
            hardware_found = False

        return self.renderer.render("edithardware.html", hardware=hardware,
                                    platforms=platforms, title=page_title, hardware_found=hardware_found)
