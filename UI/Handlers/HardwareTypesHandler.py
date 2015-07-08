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

import UI.Handlers.AuthenticatedHandler as ah


class HardwareTypesHandler(ah.AuthenticatedHandler):
    """Handle requests for the Hardware Types page"""
    
    def get_page(self, params):
        """Handle requests for the Hardware Types page
        :param params: An empty dictionary
        """
        super().get_page(params)

        def interactor_get(interactor_type):
            interactor = self.interactor_factory.create(interactor_type)
            return interactor.execute()

        hardware_types = interactor_get("GetHardwareTypeListInteractor")
        suggested_hardware_types = interactor_get("GetSuggestedHardwareTypesInteractor")

        return self.renderer.render("hardwaretypes.html", title="Manage Hardware Types", 
                                    hardware_types=hardware_types, suggested_hardware_types=suggested_hardware_types)
