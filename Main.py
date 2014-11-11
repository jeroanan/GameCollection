from Tests.Interactors.InteractorFactory import InteractorFactory
from UI.WebServer import WebServer

if __name__ == "__main__":
    ui = WebServer()
    ui.start(InteractorFactory())