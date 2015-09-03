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

import json

import HardwareType as ht
import Interactors.HardwareInteractors as hi
import UI.Handlers.AuthenticatedHandler as ah


class DeleteHardwareTypeHandler(ah.AuthenticatedHandler):
    """Handle requests to delete a hardware type""" 
    
    def get_page(self, params):
        """
        Handle requests to delete a hardware type

        Args:
            + params: A dictionary containing the details of the hardware type to be deleted. This must contain:
                   
                      + id: The id of the hardware type to be deleted

        Returns: A json object with a singe field: result. Values of result can be:

                 + ok: The deletion was successful

                 Only in the case of ok will the deletion have taken place.
        """ 
        super().get_page(params)

        result = {'result': ''}

        interactor = self.interactor_factory.create("DeleteHardwareTypeInteractor")
    
        try:
            interactor.execute(ht.HardwareType.from_dict(params))
            result['result'] = 'ok'
        except hi.HardwareTypeNotFoundException:
            result['result'] = 'not_found'
        except:
            result['result'] = 'error'

        return json.dumps(result)
