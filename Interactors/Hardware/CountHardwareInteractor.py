from Interactors.Interactor import Interactor


class CountHardwareInteractor(Interactor):
    def execute(self):
        return self.persistence.count_hardware()
