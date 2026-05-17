"""Handler for the Add Hardware operation"""
# Copyright (c) David Wilson 2015, 2026
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

import ui.handlers.authenticated_handler as ah


class AddHardwareHandler(ah.AuthenticatedHandler):
    """Handler for the Add Hardware operation"""

    def get_page(self, args):

        def execute_interactor(interactor_name):
            return self.interactor_factory.create(interactor_name).execute()

        platforms = execute_interactor("GetPlatformsInteractor")
        hardware_types = execute_interactor("GetHardwareTypeListInteractor")

        super().get_page(args)
        return self.renderer.render("addhardware.html",
                                    title="Add Hardware",
                                    platforms=platforms,
                                    hardware_types=hardware_types)
