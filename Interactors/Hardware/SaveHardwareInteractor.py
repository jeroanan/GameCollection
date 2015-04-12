from Interactors.Interactor import Interactor


class SaveHardwareInteractor(Interactor):

    """Tell persistence to save an item of hardware.
    param hardware: An instance of Hardware. The item of hardware to be saved.
    param user_id: The uuid of the user whose collection the item of hardware should be added to.
    returns: None
    """
    def execute(self, hardware, user_id):
        self.__validate(hardware)
        self.persistence.save_hardware(hardware, user_id)

    def __validate(self, hardware):
        if hardware is None:
            raise TypeError("hardware")
        if hardware.id != "":
            raise ValueError("Id cannot be set when saving new hardware")
        self.validate_string_field("Hardware name", hardware.name)
        self.validate_string_field("Platform", hardware.platform)
        self.validate_integer_field("Number owned", hardware.num_owned)
        self.validate_integer_field("Number boxed", hardware.num_boxed)
