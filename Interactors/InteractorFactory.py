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

import json

import Data.DataLoad as dl
import Interactors.Exceptions.UnrecognisedInteractorTypeException as uite
import Interactors.LoggingInteractor as li
import Interactors.GenreInteractors as gi
import Interactors.HardwareInteractors as hi
import Interactors.PlatformInteractors as pi


class InteractorFactory(object):

    def __init__(self, persistence, logger):
        self.__persistence = persistence
        self.__interactors = self.__load_interactors()
        self.__logger = logger

    def __load_interactors(self):
        with open("Interactors/interactors.json") as f:
            return json.load(f)["interactors"][0]    

    def create(self, interactor_type):
        """Create an Interactor of the specified type.
        :param interactor_type: A string indicating which type of Interactor should be created.
        :returns: An interactor of the specified type. If interactor_type does not correspond to a known type of 
                  interactor then an UnrecognisdInteractorTypeException is raised.
        """
        special_interactors = {
            "GetSuggestedPlatformsInteractor": (pi.GetSuggestedPlatformsInteractor, dl.load_suggested_platforms),
            "GetSuggestedGenresInteractor": (gi.GetSuggestedGenresInteractor, dl.load_suggested_genres),
            "GetSuggestedHardwareTypesInteractor": (hi.GetSuggestedHardwareTypesInteractor, 
                                                    dl.load_suggested_hardware_types)            
        }

        if interactor_type in special_interactors:
            interactor, init_value = special_interactors[interactor_type]
            return self.__initialise_interactor(interactor(init_value))
        elif interactor_type in self.__interactors:
            return self.__initialise_interactor(self.__string_to_interactor(self.__interactors[interactor_type]))

        raise uite.UnrecognisedInteractorTypeException

    def __string_to_interactor(self, interactor_type):
        try:
            module = __import__("Interactors." + interactor_type, fromlist=interactor_type)
        except ImportError:  #We're using one of the new classes to group interactors by feature.
            it = str.split(interactor_type, ".")
            module = __import__("Interactors." + it[0], fromlist=it[1])
        class_name = str.split(interactor_type, ".")[1]
        class_ = getattr(module, class_name)
        instantiated = class_()
        instantiated.persistence = self.__persistence
        return instantiated

    def __initialise_interactor(self, interactor):
        interactor.persistence = self.__persistence
        if isinstance(interactor, li.LoggingInteractor):
            interactor.logger = self.__logger
        return interactor
