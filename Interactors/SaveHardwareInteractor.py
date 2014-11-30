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
        if hardware.name is None or hardware.name.strip() == "":
            raise ValueError("Hardware name must be set")
        if hardware.platform is None or hardware.platform.strip() == "":
            raise ValueError("Platform must be set")
        if not str(hardware.numowned).isdigit():
            raise ValueError("Number owned must be set")
        if not str(hardware.numboxed).isdigit():
            raise ValueError("Number boxed must be set")
