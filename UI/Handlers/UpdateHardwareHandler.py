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
# along with Icarus.  If not, see <http://www.gnu.org/licenses/.>

import cherrypy
from Hardware import Hardware
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UpdateHardwareHandler(AuthenticatedHandler):
    """Handle requests to update hardware details"""
    
    def get_page(self, params):
        """Handles Hardware Update requests (i.e. new values to save to a hardware record).
        This is really intended to be used as an ajax request rather than a webpage, so
        it doesn't give much in the way of user feedback. If the user is not currently logged
        in then it will redirect to the homepage.
        param params: A dictionary comprised of the following keys:
        + id -- The uuid of the item of hardware to save.
        + name -- The name of the item of hardware. Mandatory.
        + platform -- The plaform of the item of hardware. Mandatory.
        + numcopies -- The number of copies owned of the item of hardware.
        + numboxed -- The number of boxed copies owned of the item of hardware.
        + notes -- Miscellaneous notes added by the user.
        returns: If one of the mandatory args keys is omitted then an empty string. Else None.
        """
        super().get_page(params)
        if not self.validate_params(params, ["name", "platform"]):
            return ""
        interactor = self.interactor_factory.create("UpdateHardwareInteractor")
        interactor.execute(Hardware.from_dict(params), self.session.get_value("user_id"))
