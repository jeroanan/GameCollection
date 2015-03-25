from Interactors.Interactor import Interactor


class GetHardwareDetailsInteractor(Interactor):
    def execute(self, hardware_id):
        self.__validate(hardware_id)
        return self.persistence.get_hardware_details(hardware_id)

    def __validate(self, hardware_id):
        if hardware_id is None:
            raise TypeError("hardware_id")
