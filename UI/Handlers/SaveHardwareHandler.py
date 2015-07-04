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


class SaveHardwareHandler(AuthenticatedHandler):

    """Handles Hardware Save requests.
    This is really intended to be used as an ajax request rather than a webpage, so
    it doesn't give much in the way of user feedback. If the user is not currently logged
    in then it will redirect to the homepage.
    :param args: A dictionary containing the following keys:
                 + name --  The name of the hardware. Mandatory.
                 + platform -- The hardware's platform. Mandatory.
                 + numcopies -- The number owned. Mandatory.
                 + numboxed -- The number owned boxed
                 + notes -- any other notes made by the user
    :returns: If one of the mandatory fields is omitted then an empty string is returned. Else None.
    """
    def get_page(self, params):
        super().get_page(params)
        if not self.validate_params(params, ["name", "platform", "numcopies"]):
            return ""
        interactor = self.interactor_factory.create("SaveHardwareInteractor")
        hardware = Hardware.from_dict(params)
        interactor.execute(hardware=hardware, user_id=self.session.get_value("user_id"))

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.name = params.get("name", "")
        hardware.platform = params.get("platform", "")
        hardware.num_owned = params.get("numcopies", "")
        hardware.num_boxed = params.get("numboxed", "")
        hardware.notes = params.get("notes", "")
        return hardware
