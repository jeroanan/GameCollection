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

import json

import HardwareType as ht
import Interactors.HardwareInteractors as hi
import UI.Handlers.AuthenticatedHandler as ah


class AddHardwareTypeHandler(ah.AuthenticatedHandler):
    """Handle requests to add a hardware type"""
    
    def get_page(self, args):
        """
        Handle requests to add a hardware type
        
        Args:
            args: A dictionary containing the following keys:
        
                  + name: The name of the new hardware type
                  + description: The description of the new hardware type

        Returns:
            A json object with one field: result. Values of result can be:
                  
                  + validation_failed -- Validation of args failed
                  + ok -- The hardware type was added successfully.

            Only in the case of ok will the hardware type have been added.
        """
        super().get_page(args)

        def validate():
            required_fields = ['name', 'description']
            return self.validate_params(args, required_fields)

        def save_hardware_type():
            interactor = self.interactor_factory.create('AddHardwareTypeInteractor')
            interactor.execute(ht.HardwareType.from_dict(args))

        result = {'result': ''}

        if not validate():
            result['result'] = 'validation_failed'
        else:
            try:
                save_hardware_type()
                result['result'] = 'ok'
            except hi.HardwareTypeExistsException:
                result['result'] = 'already_exists'
            except:
                result['result'] = 'error'

        return json.dumps(result)
