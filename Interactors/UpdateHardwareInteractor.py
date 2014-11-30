from Interactors.Interactor import Interactor


class UpdateHardwareInteractor(Interactor):

    def execute(self, hardware):
        self.__validate(hardware)
        self.persistence.update_hardware(hardware)

    def __validate(self, hardware):
        if hardware is None:
            raise TypeError("hardware")
        self.validate_string_field("hardware name", hardware.name)
        self.validate_string_field("platform", hardware.platform)
        self.validate_integer_field("Number owned", hardware.numowned)
        self.validate_integer_field("Number boxed", hardware.numboxed)
