from UI.Handlers.Handler import Handler


class EditHardwareHandler(Handler):

    def get_page(self, args):
        get_hardware_details_interactor = self.interactor_factory.create("GetHardwareDetailsInteractor")
        get_platforms_interactor = self.interactor_factory.create("GetPlatformsInteractor")

        hardware = get_hardware_details_interactor.execute(args.get("hardwareid", ""))
        platforms = get_platforms_interactor.execute()

        return self.renderer.render("edithardware.html", hardware=hardware, platforms=platforms, title="Edit Hardware")
