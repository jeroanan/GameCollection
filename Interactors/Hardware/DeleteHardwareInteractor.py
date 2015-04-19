from Interactors.Interactor import Interactor


class DeleteHardwareInteractor(Interactor):

    """Tells the interactor to delete the given item of hardware.
    param hardware_id: The uuid of the item of hardware to be deleted
    param user_id: The uuid of the current user
    """
    def execute(self, hardware_id, user_id):
        self.__validate(hardware_id)
        self.persistence.delete_hardware(hardware_id, user_id)

    def __validate(self, hardware_id):
        if hardware_id is None:
            raise TypeError("hardware_id")
        self.validate_string_field("Hardware id", hardware_id)
