class IndexHandler(object):

    def __init__(self, interactor_factory, renderer):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer

    def get_page(self):
        interactor = self.__interactor_factory.create("GetGamesInteractor")
        games = interactor.execute()
        return self.__renderer.render("index.html", games=games, title="Games Collection")
