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

from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class DeleteHardwareHandler(AuthenticatedHandler):

    """Handles Delete Hardware requests.
    This is really intended to be used as an ajax request rather than a webpage, so
    it doesn't give much in the way of user feedback. If the user is not currently logged
    in then it will redirect to the homepage.
    param args: A dictionary containing the key "id". id contains the uuid 
    of the item of hardware to be deleted.
    returns: If id is blank or there is an error then an empty string. Else None.
    """
    def get_page(self, args):
        super().get_page(args)
        if not self.validate_params(args, ["id"]):
            return ""

        interactor = self.interactor_factory.create("DeleteHardwareInteractor")
        try:            
            interactor.execute(args.get("id", ""), self.session.get_value("user_id"))
        except:
            return ""
