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

import Interactors.PlatformInteractors as pi
import Platform as p
import UI.Handlers.AuthenticatedHandler as ah


class AddPlatformHandler(ah.AuthenticatedHandler):
    """Handle requests to add a platform"""

    def get_page(self, args):
        """
        Handle requests to add a platform
        :param args: A dictionary containing the following keys:
                        + name
                        + description
        :returns: A json string containing one key: 'result'. Values can be:
                  + ok -- the new platform was added successfully
                  + validation_failed -- validation of args failed
                  + already_exists -- a platform with the same name already exists
                  + error -- some other error occurred while trying to add the new platform
         
                  The platform was only added if result is 'ok' 
        """
        super().get_page(args)

        result = {'result': ''}

        if not self.validate_params(args, ['name']):
            result['result'] = 'validation_failed'
        else:
            interactor = self.interactor_factory.create('AddPlatformInteractor')
            
            try:
                interactor.execute(p.Platform.from_dict(args))
                result['result'] = 'ok'
            except pi.PlatformExistsException:
                result['result'] = 'already_exists'
            except:
                result['result'] = 'error'

        return json.dumps(result)
