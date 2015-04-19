from Interactors.Interactor import Interactor


class GetHardwareDetailsInteractor(Interactor):

    """Requests the details of a specific item of hardware from persistence.
    param hardware_id: The uuid of the item of hardware to retrieve.
    param user_id: The uuid of the current user.
    returns: An instance of Hardware containing the requested item of hardware.
    """
    def execute(self, hardware_id, user_id):
        self.__validate(hardware_id)
        return self.persistence.get_hardware_details(hardware_id, user_id)

    def __validate(self, hardware_id):
        if hardware_id is None:
            raise TypeError("hardware_id")
