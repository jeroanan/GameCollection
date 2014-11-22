from UI.Handlers.Handler import Handler


class EditHardwareHandler(Handler):

    def get_page(self, hardware_id):
        interactor = self.interactor_factory.create("GetHardwareDetailsInteractor")
        hardware = interactor.execute(hardware_id)
        return self.renderer.render("edithardware.html", hardware=hardware, title="Edit Hardware")
