from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Tests.Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException


class InteractorFactory(object):

    def __init__(self, gateway):
        self.__gateway = gateway

    def create(self, interactor_type):

        if interactor_type == "AddGameInteractor":
            return self.__initialise_interactor(AddGameInteractor())
        elif interactor_type == "GetGamesInteractor":
            return self.__initialise_interactor(GetGamesInteractor())

        raise UnrecognisedInteractorTypeException

    def __initialise_interactor(self, interactor):
        interactor.games_gateway = self.__gateway
        return interactor
