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

import Persistence.Exceptions.HardwareNotFoundException as hnfe
import UI.Handlers.AuthenticatedHandler as ah


class EditHardwareHandler(ah.AuthenticatedHandler):

    
    def get_page(self, args):
        """The Edit Hardware page.
        param args: A dictionary containing the keys:
                   + 'hardwareid' -- the uuid of the hardware item to be edited
        return: The rendered Edit Hardware page. 
        If the hardware is not found then a "Hardware Not Found" message is displayed to the user.
        """
        super().get_page(args)
        create_interactor = lambda x: self.interactor_factory.create(x)
        get_hardware_details_interactor = create_interactor("GetHardwareDetailsInteractor")
        get_platforms_interactor = create_interactor("GetPlatformsInteractor")
        get_hardware_types_list_interactor = create_interactor("GetHardwareTypeListInteractor")

        hardware = []
        hardware_types = []
        platforms = []
        page_title = "Edit Hardware"
        hardware_found = True

        try:
            hardware = get_hardware_details_interactor.execute(args.get("hardwareid", ""), 
                                                               self.session.get_value("user_id"))
            hardware_types = get_hardware_types_list_interactor.execute()
            platforms = get_platforms_interactor.execute()
        except hnfe.HardwareNotFoundException:
            page_title = "Hardware Not Found"
            hardware_found = False

        return self.renderer.render("edithardware.html", hardware=hardware,
                                    platforms=platforms, hardware_types=hardware_types, title=page_title,
                                    hardware_found=hardware_found)
