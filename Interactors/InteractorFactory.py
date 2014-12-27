from Data.SuggestedPlatforms import SuggestedPlatforms
from Interactors.AddGenreInteractor import AddGenreInteractor
from Interactors.CountGamesInteractor import CountGamesInteractor
from Interactors.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.GetGenreInteractor import GetGenreInteractor
from Interactors.GetGenresInteractor import GetGenresInteractor
from Interactors.GetHardwareInteractor import GetHardwareDetailsInteractor
from Interactors.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.AddPlatformInteractor import AddPlatformInteractor
from Interactors.DeleteGameInteractor import DeleteGameInteractor
from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.GetGameInteractor import GetGameInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.GetPlatformInteractor import GetPlatformInteractor
from Interactors.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.SaveHardwareInteractor import SaveHardwareInteractor
from Interactors.SearchInteractor import SearchInteractor
from Interactors.UpdateGameInteractor import UpdateGameInteractor
from Interactors.UpdateGenreInteractor import UpdateGenreInteractor
from Interactors.UpdateHardwareInteractor import UpdateHardwareInteractor
from Tests.Interactors.TestDeleteGenreInteractor import DeleteGenreInteractor
from Tests.Interactors.TestUpdatePlatformInteractor import UpdatePlatformInteractor


class InteractorFactory(object):

    def __init__(self, persistence):
        self.__persistence = persistence

        self.__interactors = {
            "AddGameInteractor": self.__initialise_interactor(AddGameInteractor()),
            "GetGamesInteractor": self.__initialise_interactor(GetGamesInteractor()),
            "GetPlatformsInteractor": self.__initialise_interactor(GetPlatformsInteractor()),
            "AddPlatformInteractor": self.__initialise_interactor(AddPlatformInteractor()),
            "GetGameInteractor": self.__initialise_interactor(GetGameInteractor()),
            "UpdateGameInteractor":  self.__initialise_interactor(UpdateGameInteractor()),
            "DeleteGameInteractor": self.__initialise_interactor(DeleteGameInteractor()),
            "GetHardwareListInteractor": self.__initialise_interactor(GetHardwareListInteractor()),
            "SaveHardwareInteractor": self.__initialise_interactor(SaveHardwareInteractor()),
            "GetPlatformInteractor": self.__initialise_interactor(GetPlatformInteractor()),
            "UpdatePlatformInteractor": self.__initialise_interactor(UpdatePlatformInteractor()),
            "DeletePlatformInteractor": self.__initialise_interactor(DeletePlatformInteractor()),
            "GetHardwareDetailsInteractor": self.__initialise_interactor(GetHardwareDetailsInteractor()),
            "UpdateHardwareInteractor": self.__initialise_interactor(UpdateHardwareInteractor()),
            "DeleteHardwareInteractor": self.__initialise_interactor(DeleteHardwareInteractor()),
            "GetSuggestedPlatformsInteractor":
                self.__initialise_interactor(GetSuggestedPlatformsInteractor(SuggestedPlatforms())),
            "GetGenresInteractor": self.__initialise_interactor(GetGenresInteractor()),
            "AddGenreInteractor": self.__initialise_interactor(AddGenreInteractor()),
            "GetGenreInteractor": self.__initialise_interactor(GetGenreInteractor()),
            "UpdateGenreInteractor": self.__initialise_interactor(UpdateGenreInteractor()),
            "DeleteGenreInteractor": self.__initialise_interactor(DeleteGenreInteractor()),
            "CountGamesInteractor": self.__initialise_interactor(CountGamesInteractor()),
            "SearchInteractor": self.__initialise_interactor(SearchInteractor())
        }

    def __initialise_interactor(self, interactor):
        interactor.persistence = self.__persistence
        return interactor

    def create(self, interactor_type):
        if interactor_type in self.__interactors:
            return self.__interactors[interactor_type]

        raise UnrecognisedInteractorTypeException
