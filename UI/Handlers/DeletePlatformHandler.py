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

import UI.Handlers.AuthenticatedHandler as ah


class DeletePlatformHandler(ah.AuthenticatedHandler):
    # Handles requests to delete a platform

    def get_page(self, params):
        """Handles requests to delete a platform
        :param params: A dictionary. It is expected to contain the following:
                       * id -- the id of the platform to be deleted
        """
        super().get_page(params)

        if not self.validate_params(params, ["id"]):
            return ""

        interactor = self.interactor_factory.create("DeletePlatformInteractor")
        interactor.execute(params.get("id", params.get("id", "")))
        
