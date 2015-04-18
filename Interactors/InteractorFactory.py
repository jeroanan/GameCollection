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

from Data.LoadSuggestedPlatforms import LoadSuggestedPlatforms
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.LoggingInteractor import LoggingInteractor
from Interactors.Platform.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor


class InteractorFactory(object):

    def __init__(self, persistence, logger):
        self.__persistence = persistence
        self.__interactors = self.__load_interactors()
        self.__logger = logger

    def __load_interactors(self):
        with open("Interactors/interactors.json") as f:
            return json.load(f)["interactors"][0]    

    def create(self, interactor_type):
        if interactor_type == "GetSuggestedPlatformsInteractor":
            return self.__initialise_interactor(GetSuggestedPlatformsInteractor(LoadSuggestedPlatforms()))

        if interactor_type in self.__interactors:
            return self.__initialise_interactor(self.__string_to_interactor(self.__interactors[interactor_type]))

        raise UnrecognisedInteractorTypeException

    def __string_to_interactor(self, interactor_type):
        module = __import__("Interactors." + interactor_type, fromlist=interactor_type)
        class_name = str.split(interactor_type, ".")[1]
        class_ = getattr(module, class_name)
        instantiated = class_()
        instantiated.persistence = self.__persistence
        return instantiated

    def __initialise_interactor(self, interactor):
        interactor.persistence = self.__persistence

        if isinstance(interactor, LoggingInteractor):
            interactor.logger = self.__logger
        return interactor
