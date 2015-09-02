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

import Interactors.HardwareInteractors as hi
import HardwareType as ht
import UI.Handlers.AuthenticatedHandler as ah


class UpdateHardwareTypeHandler(ah.AuthenticatedHandler):
    """Handle requests to update a hardware type"""

    def get_page(self, params):
        """
        Handle requests to update a hardware type

        Args:
            params: A dictionary containing the following keys:
             
                    + id: The id of the hardware type to be updated
                    + name: The name of the hardware type to be updated
                    + description: The description of the hardware type to be updated

        Returns:
            A json object with one field: result. Values of result can be:

                 + validation_failed -- either hardware_type is None, or one of its keys is None or an empty string
                 + ok -- The hardware type was updated successfully

            Only in the case of ok will the hardware type have been updated.
        """
        super().get_page(params)

        def validate():
            
            required_params = ['id', 'name']
            
            if params is None:
                return False

            if not self.validate_params(params, required_params):
                return False
            
            return True

        result = {'result': ''}

        if not validate():
            result['result'] = 'validation_failed'
        else:
            interactor = self.interactor_factory.create("UpdateHardwareTypeInteractor") 

            try:
                interactor.execute(ht.HardwareType.from_dict(params))
                result['result'] = 'ok'
            except hi.HardwareTypeExistsException:
                result['result'] = 'already_exists'
            except hi.HardwareTypeNotFoundException:
                result['result'] = 'not_found'
            except:
                result['result'] = 'error'

        return json.dumps(result)
