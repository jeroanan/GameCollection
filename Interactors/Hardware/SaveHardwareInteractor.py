# Copyright (c) David Wilson 2015
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


class SaveHardwareInteractor(Interactor):
    # Logic for saving hardware
    
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
