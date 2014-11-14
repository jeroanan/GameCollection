from Interactors.Interactor import Interactor


class SaveHardwareInteractor(Interactor):
    def execute(self, hardware):
        self.persistence.save_hardware(hardware)
