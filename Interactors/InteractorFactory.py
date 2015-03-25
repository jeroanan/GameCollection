from Data.LoadSuggestedPlatforms import LoadSuggestedPlatforms
from Interactors.Genre.AddGenreInteractor import AddGenreInteractor
from Interactors.Game.CountGamesInteractor import CountGamesInteractor
from Interactors.Hardware.CountHardwareInteractor import CountHardwareInteractor
from Interactors.Hardware.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.Platform.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.Genre.GetGenreInteractor import GetGenreInteractor
from Interactors.Genre.GetGenresInteractor import GetGenresInteractor
from Interactors.Hardware.GetHardwareInteractor import GetHardwareDetailsInteractor
from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Platform.AddPlatformInteractor import AddPlatformInteractor
from Interactors.Game.DeleteGameInteractor import DeleteGameInteractor
from Interactors.Game.AddGameInteractor import AddGameInteractor
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.Game.GetGameInteractor import GetGameInteractor
from Interactors.Game.GetGamesInteractor import GetGamesInteractor
from Interactors.Platform.GetPlatformInteractor import GetPlatformInteractor
from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.Platform.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.Hardware.SaveHardwareInteractor import SaveHardwareInteractor
from Interactors.SearchInteractor import SearchInteractor
from Interactors.Game.UpdateGameInteractor import UpdateGameInteractor
from Interactors.Genre.UpdateGenreInteractor import UpdateGenreInteractor
from Interactors.Hardware.UpdateHardwareInteractor import UpdateHardwareInteractor
from Interactors.User.LoginInteractor import LoginInteractor
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
                self.__initialise_interactor(GetSuggestedPlatformsInteractor(LoadSuggestedPlatforms())),
            "GetGenresInteractor": self.__initialise_interactor(GetGenresInteractor()),
            "AddGenreInteractor": self.__initialise_interactor(AddGenreInteractor()),
            "GetGenreInteractor": self.__initialise_interactor(GetGenreInteractor()),
            "UpdateGenreInteractor": self.__initialise_interactor(UpdateGenreInteractor()),
            "DeleteGenreInteractor": self.__initialise_interactor(DeleteGenreInteractor()),
            "CountGamesInteractor": self.__initialise_interactor(CountGamesInteractor()),
            "SearchInteractor": self.__initialise_interactor(SearchInteractor()),
            "CountHardwareInteractor": self.__initialise_interactor(CountHardwareInteractor()),
            "LoginInteractor": self.__initialise_interactor(LoginInteractor())
        }

    def __initialise_interactor(self, interactor):
        interactor.persistence = self.__persistence
        return interactor

    def create(self, interactor_type):
        if interactor_type in self.__interactors:
            return self.__interactors[interactor_type]

        raise UnrecognisedInteractorTypeException
