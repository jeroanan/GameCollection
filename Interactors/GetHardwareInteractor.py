from Interactors.Interactor import Interactor


class GetHardwareDetailsInteractor(Interactor):
    def execute(self, platform_id):
        self.persistence.get_hardware_details(platform_id)
