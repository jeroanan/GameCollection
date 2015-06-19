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

import HardwareType as ht
import UI.Handlers.AuthenticatedHandler as ah


class AddHardwareTypeHandler(ah.AuthenticatedHandler):
    
    def get_page(self, args):
        super().get_page(args)
        interactor = self.interactor_factory.create("AddHardwareTypeInteractor")
        interactor.execute(ht.HardwareType.from_dict(args))
