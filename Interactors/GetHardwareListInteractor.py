from Interactors.Interactor import Interactor


class GetHardwareListInteractor(Interactor):
    def execute(self):
        return self.persistence.get_hardware_list()
