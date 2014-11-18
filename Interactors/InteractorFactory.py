from Interactors.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.AddPlatformInteractor import AddPlatformInteractor
from Interactors.DeleteGameInteractor import DeleteGameInteractor
from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.GetGameInteractor import GetGameInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.GetPlatformInteractor import GetPlatformInteractor
from Interactors.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.SaveHardwareInteractor import SaveHardwareInteractor
from Interactors.UpdateGameInteractor import UpdateGameInteractor


class InteractorFactory(object):

    def __init__(self, persistence):
        self.__persistence = persistence

    def create(self, interactor_type):

        if interactor_type == "AddGameInteractor":
            return self.__initialise_interactor(AddGameInteractor())
        elif interactor_type == "GetGamesInteractor":
            return self.__initialise_interactor(GetGamesInteractor())
        elif interactor_type == "GetPlatformsInteractor":
            return self.__initialise_interactor(GetPlatformsInteractor())
        elif interactor_type == "AddPlatformInteractor":
            return self.__initialise_interactor(AddPlatformInteractor())
        elif interactor_type == "GetGameInteractor":
            return self.__initialise_interactor(GetGameInteractor())
        elif interactor_type == "UpdateGameInteractor":
            return self.__initialise_interactor(UpdateGameInteractor())
        elif interactor_type == "DeleteGameInteractor":
            return self.__initialise_interactor(DeleteGameInteractor())
        elif interactor_type == "GetHardwareListInteractor":
            return self.__initialise_interactor(GetHardwareListInteractor())
        elif interactor_type == "SaveHardwareInteractor":
            return self.__initialise_interactor(SaveHardwareInteractor())
        elif interactor_type == "GetPlatformInteractor":
            return self.__initialise_interactor(GetPlatformInteractor())

        raise UnrecognisedInteractorTypeException

    def __initialise_interactor(self, interactor):
        interactor.persistence = self.__persistence
        return interactor
