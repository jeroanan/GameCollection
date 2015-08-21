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

import Interactors.Interactor as interactor
import Interactors.Game.Params.GetGamesInteractorParams as ggip
import Interactors.Hardware.Params.GetHardwareListInteractorParams as ghlip


class ExportCollectionInteractor(interactor.Interactor):
    
    def __init__(self, interactor_factory):
        self.__interactor_factory = interactor_factory

    def execute(self, data_sets_to_export, user_id):
        """Get data to export
        :param data_sets_to_export: A list of data sets to export
        :param user_id: The user id to export data for
        :returns: A dictionary containing the exported data
        """
        interactor_constructors = {
            'games': ('GetGamesInteractor', ggip.GetGamesInteractorParams),
            'hardware': ('GetHardwareListInteractor', ghlip.GetHardwareListInteractorParams)
        }

        data = {}

        for ds in data_sets_to_export:
            if ds in interactor_constructors:
                interactor_type, p = interactor_constructors[ds]
                interactor = self.__interactor_factory.create(interactor_type)
                params = p()
                params.user_id = user_id
                data[ds] = interactor.execute(params)                

        return data
