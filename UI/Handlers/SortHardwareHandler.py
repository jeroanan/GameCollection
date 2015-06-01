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

from Interactors.Hardware.Params.GetHardwareListInteractorParams import GetHardwareListInteractorParams
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class SortHardwareHandler(AuthenticatedHandler):
    """Sorts a list of all of the user's hardware."""

    def get_page(self, args):
        """Sorts a list of all of the user's hardware.
        :param args: A dictionary containing the following keys:
                     * field
                     * sortdir
        :returns: A rendered page containing the sorted hardware list"""
        super().get_page(args)
        interactor = self.interactor_factory.create("GetHardwareListInteractor")
        
        params = GetHardwareListInteractorParams()
        params.sort_field = args.get("field", "name")
        params.sort_direction = args.get("sortdir", "")
        params.user_id = self.session.get_value("user_id")
        
        hardware = interactor.execute(params)

        return self.renderer.render("hardware.html", hardware=hardware, hw_sort_field=args.get("field", ""),
                                    hw_sort_dir=args.get("sortdir", ""))
