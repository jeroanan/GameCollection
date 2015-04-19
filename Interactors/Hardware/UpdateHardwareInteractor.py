from Interactors.Interactor import Interactor


class UpdateHardwareInteractor(Interactor):

    """Tell persistence to update the given item of hardware
    param hardware: An instance of Hardware. The item of hardware to be updated.
    param user_id: The uuid of the current user.
    returns: None
    """
    def execute(self, hardware, user_id):
        self.__validate(hardware)
        self.persistence.update_hardware(hardware, user_id)

    def __validate(self, hardware):
        if hardware is None:
            raise TypeError("hardware")
        self.validate_string_field("hardware name", hardware.name)
        self.validate_string_field("platform", hardware.platform)
        self.validate_integer_field("Number owned", hardware.num_owned)
        self.validate_integer_field("Number boxed", hardware.num_boxed)
