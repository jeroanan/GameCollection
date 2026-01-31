"""Handler for editing an existing hardware type"""
# Copyright (c) 2015, 2026 David Wilson
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

import hardware_type as ht
import UI.Handlers.AuthenticatedHandler as ah


class EditHardwareTypeHandler(ah.AuthenticatedHandler):
    """Handler for editing an existing hardware type"""

    def get_page(self, params):
        super().get_page(params)
        interactor = self.interactor_factory.create("GetHardwareTypeInteractor")
        hardware_type = interactor.execute(ht.HardwareType.from_dict(params))
        return self.renderer.render(
            "edithardwaretype.html",
            title="Edit Hardware Type",
            hardware_type=hardware_type)
