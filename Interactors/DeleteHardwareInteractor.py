from Interactors.Interactor import Interactor


class DeleteHardwareInteractor(Interactor):

    def execute(self, hardware_id):
        self.__validate(hardware_id)
        self.persistence.delete_hardware(hardware_id)

    def __validate(self, hardware_id):
        if hardware_id is None:
            raise TypeError("hardware_id")
        self.validate_string_field("Hardware id", hardware_id)
