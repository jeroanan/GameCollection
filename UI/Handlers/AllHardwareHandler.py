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

from Interactors.Hardware.Params.GetHardwareListInteractorParams import GetHardwareListInteractorParams
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AllHardwareHandler(AuthenticatedHandler):
    """The All Hardware page"""
    
    def get_page(self, args):
        """The All Hardware page
        Shows a list of all the hardware that the current user has in their collection.
        param args: Seems not to be currently used.
        returns: The rendered all hardware page
        """
        super().get_page(args)
        interactor = self.interactor_factory.create("GetHardwareListInteractor")

        params = GetHardwareListInteractorParams.from_dict({
            "platform": args.get("platform", ""),
            "sort_field": "name",
            "sort_direction": "asc",
            "user_id": self.session.get_value("user_id")})

        hardware = interactor.execute(params)
        return self.renderer.render("allhardware.html", hardware=hardware, title="All Hardware",
                                    hw_sort_field="name", hw_sort_dir="asc")
