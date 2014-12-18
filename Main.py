from Data.Config import Config
from Interactors.InteractorFactory import InteractorFactory
from Persistence.MongoPersistence import MongoPersistence
from UI.WebServer import WebServer

if __name__ == "__main__":
    persistence = MongoPersistence()
    config = Config()
    interactor_factory = InteractorFactory(persistence)

    ui = WebServer()
    ui.start(interactor_factory=interactor_factory, config=config)