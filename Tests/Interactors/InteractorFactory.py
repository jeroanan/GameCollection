from GamesGateway import GamesGateway
from GetGamesInteractor import GetGamesInteractor
from Interactors.AddGameInteractor import AddGameInteractor
from Tests.Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException


class InteractorFactory(object):

    def create(self, interactor_type):

        if interactor_type == "AddGameInteractor":
            return self.__initialise_interactor(AddGameInteractor())
        elif interactor_type == "GetGamesInteractor":
            return self.__initialise_interactor(GetGamesInteractor())

        raise UnrecognisedInteractorTypeException

    def __initialise_interactor(self, interactor):
        interactor.games_gateway = GamesGateway()
        return interactor
