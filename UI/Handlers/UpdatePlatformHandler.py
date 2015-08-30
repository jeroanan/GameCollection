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

import Platform as p
import Interactors.PlatformInteractors as pi
import UI.Handlers.AuthenticatedHandler as ah


class UpdatePlatformHandler(ah.AuthenticatedHandler):
    """Handle requests to update an existing platform"""

    def get_page(self, params):
        """
        Handle requests to update an existing platform
        :param params: A dictionary containing details of the platform to be updated
        :returns: A json object with one key, result, containing the result of the update operation. This can be:
                  + ok -- Update was ok
                  + validation_failed -- Validation of params failed
                  + alread_exists -- the platform to be updated already exists with a different id
                  + not_found -- the platform to be updated does not exist
                  + error -- some other error occurred
          
                  Only in the case of ok will the record have been updated.
        """
        super().get_page(params)
        result = {'result': ''}

        if not self.__validate_params(params):
            result['result'] = 'validation_failed'
        else:
            interactor = self.interactor_factory.create("UpdatePlatformInteractor")
            platform = p.Platform.from_dict(params)

            try:
                interactor.execute(platform=platform)
                result['result'] = 'ok'
            except pi.PlatformExistsException:
                result['result'] = 'already_exists'
            except pi.PlatformNotFoundException:
                result['result'] = 'not_found'
            except Exception:
                result['result'] = 'error'
        
        return json.dumps(result)

    def __validate_params(self, params):
        if params is None:
            return False
        return self.validate_params(params, ["id", "name"])
    
