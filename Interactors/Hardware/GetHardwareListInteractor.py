from Interactors.Interactor import Interactor


class GetHardwareListInteractor(Interactor):

    """Request a list of the user's hardware from persistence
    param sort_field: The field to sort the hardware on
    param sort_direction: The order to sort the hardware in
    param user_id: The uuid of the user
    returns: A list of instances of Hardware 
    """
    def execute(self, sort_field, sort_direction, user_id):
        return self.persistence.get_hardware_list(sort_field=sort_field, sort_direction=sort_direction, user_id=user_id)
