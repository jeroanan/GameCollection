from Interactors.Interactor import Interactor


class DeleteHardwareInteractor(Interactor):
    def execute(self, hardware_id):
        self.persistence.delete_hardware(hardware_id)
