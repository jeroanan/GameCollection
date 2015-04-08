from Persistence.Exceptions.HardwareNotFoundException import HardwareNotFoundException
from UI.Handlers.Handler import Handler


class EditHardwareHandler(Handler):

    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()
        get_hardware_details_interactor = self.interactor_factory.create("GetHardwareDetailsInteractor")
        get_platforms_interactor = self.interactor_factory.create("GetPlatformsInteractor")

        hardware = []
        platforms = []
        page_title = "Edit Hardware"
        hardware_found = True

        try:
            hardware = get_hardware_details_interactor.execute(args.get("hardwareid", ""))
            platforms = get_platforms_interactor.execute()
        except HardwareNotFoundException:
            page_title = "Hardware Not Found"
            hardware_found = False

        return self.renderer.render("edithardware.html", hardware=hardware,
                                    platforms=platforms, title=page_title, hardware_found=hardware_found)
