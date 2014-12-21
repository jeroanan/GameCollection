from Interactors.Interactor import Interactor


class GetHardwareListInteractor(Interactor):
    def execute(self, sort_field, sort_direction):
        return self.persistence.get_hardware_list(sort_field=sort_field, sort_direction=sort_direction)
