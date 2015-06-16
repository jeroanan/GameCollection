# Copyright (c) 2015 David Wilson
# This file is part of Icarus.

# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

from Interactors.Interactor import Interactor


class AddHardwareTypeInteractor(Interactor):
    
    def execute(self, hardware_type):
        self.persistence.add_hardware_type(hardware_type)

class CountHardwareInteractor(Interactor):
    """Count the items of hardware in the system"""

    def execute(self, user_id):
        """Count the items of hardware in the system
        :returns: The number of items of hardware in the system"""
        return self.persistence.count_hardware(user_id)


class DeleteHardwareInteractor(Interactor):
    """Delete an item of hardware"""
    
    def execute(self, hardware_id, user_id):
        """Tells the interactor to delete the given item of hardware.
        param hardware_id: The uuid of the item of hardware to be deleted
        param user_id: The uuid of the current user
        """
        self.__validate(hardware_id)
        self.persistence.delete_hardware(hardware_id, user_id)

    def __validate(self, hardware_id):
        if hardware_id is None:
            raise TypeError("hardware_id")
        self.validate_string_field("Hardware id", hardware_id)


class GetHardwareDetailsInteractor(Interactor):
    """Get details of a specific item of hardware"""
    
    def execute(self, hardware_id, user_id):
        """Requests the details of a specific item of hardware from persistence.
        param hardware_id: The uuid of the item of hardware to retrieve.
        param user_id: The uuid of the current user.
        returns: An instance of Hardware containing the requested item of hardware.
        """
        self.__validate(hardware_id)
        return self.persistence.get_hardware_details(hardware_id, user_id)

    def __validate(self, hardware_id):
        if hardware_id is None:
            raise TypeError("hardware_id")


class GetHardwareListInteractor(Interactor):
    """Get a list of the user's hardware"""
    
    def execute(self, params):
        """Request a list of the user's hardware from persistence
        param params: An object of type GetHardwareListInteractorParams
        returns: A list of instances of Hardware 
        """
        if params.platform == "" or params.platform is None:
            return self.persistence.get_hardware_list(params)
        return self.persistence.get_hardware_list_for_platform(params)


class GetHardwareTypeListInteractor(Interactor):
    """Get a list of all hardware types stored in the system"""

    def execute(self):
         """Get a list of all hardware types stored in the system
         :returns: A list of HardwareType objects. All hardware types stored in the system.
         """
         return self.persistence.get_hardware_types_list()


class GetSuggestedHardwareTypesInteractor(Interactor):
    """Get suggested hardware types"""
    
    def __init__(self, suggested_hardware_types):
        """Initialise object state.
        :param suggested_hardware_types: A function to get the list of suggested hardware types.
        """
        self.__suggested_hardware_types = suggested_hardware_types

    def execute(self):
        """Get suggested hardware types.
        :returns: A list of HardwareType objects. The suggested hardware types not already stored in the system.
        """
        suggested_hardware_types = self.__suggested_hardware_types()
        hardware_types = self.persistence.get_hardware_types_list()
        return [s for s in suggested_hardware_types if s not in hardware_types]


class SaveHardwareInteractor(Interactor):
    """Logic for saving hardware"""
    
    def execute(self, hardware, user_id):
        """Tell persistence to save an item of hardware.
        param hardware: An instance of Hardware. The item of hardware to be saved.
        param user_id: The uuid of the user whose collection the item of hardware should be added to.
        returns: None
        """
        self.__validate(hardware)
        self.persistence.save_hardware(hardware, user_id)

    def __validate(self, hardware):
        if hardware is None:
            raise TypeError("hardware")
        if hardware.id != "":
            raise ValueError("Id cannot be set when saving new hardware")

        string_validations = {"Hardware name": hardware.name,
                              "Platform": hardware.platform}
        self.validate_string_fields(string_validations)

        integer_validations = {"Number owned": hardware.num_owned,
                               "Number boxed": hardware.num_boxed}
        self.validate_integer_fields(integer_validations)


class UpdateHardwareInteractor(Interactor):
    """Update an item of hardware"""
    
    def execute(self, hardware, user_id):
        """Tell persistence to update the given item of hardware
        :param hardware: An instance of Hardware. The item of hardware to be updated.
        :param user_id: The uuid of the current user.
        :returns: None
        """
        self.__validate(hardware)
        self.persistence.update_hardware(hardware, user_id)

    def __validate(self, hardware):
        if hardware is None:
            raise TypeError("hardware")
        self.validate_string_field("hardware name", hardware.name)
        self.validate_string_field("platform", hardware.platform)
        self.validate_integer_field("Number owned", hardware.num_owned)
        self.validate_integer_field("Number boxed", hardware.num_boxed)
