from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.GetPlatformsInteractor import GetPlatformsInteractor
from Tests.Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException


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

        raise UnrecognisedInteractorTypeException

    def __initialise_interactor(self, interactor):
        interactor.persistence = self.__persistence
        return interactor
