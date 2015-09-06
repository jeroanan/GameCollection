# Copyright (c) 2015 David Wilson
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

import Interactors.GenreInteractors as gi
import Genre as g
import UI.Handlers.AuthenticatedHandler as ah

class DeleteGenreHandler(ah.AuthenticatedHandler):
    """Handles requests to delete a genre"""

    def get_page(self, params):
        """
        Handles a request to delete a genre.

        Args:
            params: A dictionary containing the following keys:

                    + id

        Returns: A json object containing one field: result. Values of result can be:
                  
                 + ok: The deletion was successful
                 + not_found: The genre to be deleted was not found
                 + error: A miscellaneous error was encountered while deleting the genre

                Only in the case of ok will the deletion have taken place.
        """
        super().get_page(params)

        result = {'result': ''}

        if not self.validate_params(params, ['id']):
            result['result'] = 'validation_failed'
            return json.dumps(result)

        interactor = self.interactor_factory.create("DeleteGenreInteractor")

        try:
            interactor.execute(g.Genre.from_dict(params))
            result['result'] = 'ok'
        except gi.GenreNotFoundException:
            result['result'] = 'not_found'
        except:
            result['result'] = 'error'

        return json.dumps(result)
