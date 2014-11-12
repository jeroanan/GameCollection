from Interactors.InteractorFactory import InteractorFactory
from Persistence.MongoPersistence import MongoPersistence
from UI.WebServer import WebServer

if __name__ == "__main__":
    ui = WebServer()
    ui.start(InteractorFactory(MongoPersistence()))