from Interactors.Interactor import Interactor


class SaveHardwareInteractor(Interactor):

    def execute(self, hardware):
        self.__validate(hardware)
        self.persistence.save_hardware(hardware)

    def __validate(self, hardware):
        if hardware is None:
            raise TypeError("hardware")
        if hardware.id != "":
            raise ValueError("Id cannot be set when saving new hardware")
        self.validate_string_field("Hardware name", hardware.name)
        self.validate_string_field("Platform", hardware.platform)
        self.validate_integer_field("Number owned", hardware.numowned)
        self.validate_integer_field("Number boxed", hardware.numboxed)
