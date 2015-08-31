# copyright (c) David Wilson 2015
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
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

import json

import Interactors.PlatformInteractors as pi
import UI.Handlers.AuthenticatedHandler as ah


class DeletePlatformHandler(ah.AuthenticatedHandler):
    """Handles requests to delete a platform"""

    def get_page(self, params):
        """
        Handles requests to delete a platform

        Args:
            params: A dictionary. It is expected to contain the following:
                       * id -- the id of the platform to be deleted

        Returns:
            A json object with one field: result. Values of result can be:

               + validation_failed -- Validation of params failed
               + not_found -- The platform to be deleted did not exist
               + error -- A problem occurred while deleting the platform
               + ok -- Deletion was successful

           Only in the case of ok will deletion have taken place
        """
        super().get_page(params)

        result = {'result': ''}

        if not self.validate_params(params, ["id"]):
            result['result'] = 'validation_failed'
        else:
            interactor = self.interactor_factory.create("DeletePlatformInteractor")
            try:
                interactor.execute(params.get("id", params.get("id", "")))
                result['result'] = 'ok'
            except pi.PlatformNotFoundException:
                result['result'] = 'not_found'
            except:                
                result['result'] = 'error'

        return json.dumps(result)
