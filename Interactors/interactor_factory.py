"""Factory for creating interactors."""
# Copyright (c) David Wilson 2015, 2026
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

import importlib
import json

import Data.data_load as dl
import Interactors.Exceptions.unrecognised_interactor_type_exception as uite
import Interactors.collection_interactors as ci
import Interactors.LoggingInteractor as li
import Interactors.genre_interactors as gi
import Interactors.HardwareInteractors as hi
import Interactors.PlatformInteractors as pi


class InteractorFactory:
    """Factory for creating interactors."""
    def __init__(self, persistence, logger):
        self.__persistence = persistence
        self.__interactors = self.__load_interactors()
        self.__logger = logger

    def __load_interactors(self):
        with open("Interactors/interactors.json", encoding="utf-8") as f:
            return json.load(f)["interactors"][0]

    def create(self, interactor_type):
        """Create an Interactor of the specified type.
        :param interactor_type: A string indicating which type of Interactor should be created.
        :returns: An interactor of the specified type. If interactor_type does not correspond to a
                  known type of interactor then an UnrecognisedInteractorTypeException is raised.
        """
        special_interactors = {
            "GetSuggestedPlatformsInteractor": 
                (pi.GetSuggestedPlatformsInteractor, dl.load_suggested_platforms),
            "GetSuggestedGenresInteractor": 
                (gi.GetSuggestedGenresInteractor, dl.load_suggested_genres),
            "GetSuggestedHardwareTypesInteractor": 
                (hi.GetSuggestedHardwareTypesInteractor, dl.load_suggested_hardware_types)
        }

        if interactor_type in special_interactors:
            interactor, init_value = special_interactors[interactor_type]
            return self.__initialise_interactor(interactor(init_value))

        if interactor_type == "ExportCollectionInteractor":
            return ci.ExportCollectionInteractor(self)

        if interactor_type in self.__interactors:
            return self.__initialise_interactor(
                self.__string_to_interactor(self.__interactors[interactor_type]))

        raise uite.UnrecognisedInteractorTypeException

    def __string_to_interactor(self, interactor_type):
        #TODO: I Will need to clean this up at some point.
        interactors = {
            "Search.SearchInteractor": "search_interactor",
            "GameInteractors.AddGameInteractor": "game_interactors",
            "GameInteractors.CountGamesInteractor": "game_interactors",
            "GameInteractors.DeleteGameInteractor": "game_interactors",
            "GameInteractors.GetGameInteractor": "game_interactors",
            "GameInteractors.GetGamesInteractor": "game_interactors",
            "GameInteractors.UpdateGameInteractor": "game_interactors",
            "GenreInteractors.AddGenreInteractor": "genre_interactors",
            "GenreInteractors.DeleteGenreInteractor": "genre_interactors",
            "GenreInteractors.GetGenreInteractor": "genre_interactors",
            "GenreInteractors.GetGenresInteractor": "genre_interactors",
            "GenreInteractors.UpdateGenreInteractor": "genre_interactors",
        }

        print(interactor_type)
        if interactor_type in interactors:
            try:
                [mod, class_name] = str.split(interactor_type, ".")
                module = importlib.import_module(
                    f"Interactors.{mod}.{interactors[interactor_type]}")
                class_ = getattr(module, class_name)
            except ModuleNotFoundError:
                [_m, class_name] = str.split(interactor_type, ".")
                module = importlib.import_module(f"Interactors.{interactors[interactor_type]}")
                class_ = getattr(module, class_name)
        else:
            try:
                module = __import__("Interactors." + interactor_type, fromlist=interactor_type)
            except ImportError:
                #We're using one of the new classes to group interactors by feature.
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
