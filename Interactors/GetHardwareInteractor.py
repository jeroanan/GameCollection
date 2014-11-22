from Interactors.Interactor import Interactor


class GetHardwareDetailsInteractor(Interactor):
    def execute(self, hardware_id):
        return self.persistence.get_hardware_details(hardware_id)
