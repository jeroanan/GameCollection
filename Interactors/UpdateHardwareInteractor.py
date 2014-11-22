from Interactors.Interactor import Interactor


class UpdateHardwareInteractor(Interactor):
    def execute(self, hardware):
        self.persistence.update_hardware(hardware)
