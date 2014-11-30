from Interactors.Interactor import Interactor


class UpdateHardwareInteractor(Interactor):
    def execute(self, hardware):

        if hardware is None:
            raise TypeError("hardware")

        if hardware.name is None or hardware.name.strip() == "":
            raise ValueError("hardware name must be set.")
        if hardware.platform is None or hardware.platform.strip() == "":
            raise ValueError("platform must be set.")
        if not str(hardware.numowned).isdigit():
            raise ValueError("Number owned must be set.")
        if not str(hardware.numboxed).isdigit():
            raise ValueError("Number boxed must be set.")

        self.persistence.update_hardware(hardware)
