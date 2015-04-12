from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams
from Persistence.Exceptions.UnrecognisedFieldNameException import UnrecognisedFieldNameException
from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    """Constructor
    param interactor_factory: An instance of InteractorFactory
    param renderer: An instance of TemplateRenderer
    param config: An instance of Data.Config
    """
    def __init__(self, interactor_factory, renderer, config):
        super().__init__(interactor_factory, renderer)
        self.__config = config
        self.__game_sort = None
        self.__game_sort_dir = None
        self.__hardware_sort = None
        self.__hardware_sort_dir = None

    """The index page.
    Currently the index page displays a summary of the user's games and hardware. It also displays a count
    with each of these.
    param args: A dictionary that is comprised of the following keys:
                + gamesort -- a string containing the name of the column to sort the list of games by.
                + gamesortdir -- a string containing the direction the games should be sorted in.
                + hardwaresort -- a string containing the name of the column to sort the list of hardware by.
                + hardwaresortdir -- a string containing the direction that the hardware should be sorted in.
    returns: The rendered index page. If one of the sort fields is not recognised then redirect to self 
             without querystring.
    """
    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()

        self.__init_sorting(args)

        try:
            games = self.__get_games()
            hardware = self.__get_hardware()
        except UnrecognisedFieldNameException:
            raise cherrypy.HTTPRedirect("/")

        return self.renderer.render("index.html", games=games, hardware=hardware,
                                    title="Games Collection", game_sort_field=self.__game_sort,
                                    game_sort_dir=self.__game_sort_dir, hw_sort_field=self.__hardware_sort,
                                    number_of_games=(self.__count_games()),
                                    hw_sort_dir=self.__hardware_sort_dir)

    def __init_sorting(self, args):
        self.__init_game_sorting(args)
        self.__init_hardware_sorting(args)

    def __init_game_sorting(self, args):
        default_sort_field = "title"
        default_sort_direction = "asc"
        self.__game_sort = self.set_if_null(args.get("gamesort", default_sort_field), default_sort_field)
        self.__game_sort_dir = self.set_if_null(args.get("gamesortdir", default_sort_direction),
                                                default_sort_direction)

    def __init_hardware_sorting(self, args):
        default_sort_field = "name"
        default_sort_direction = "asc"
        self.__hardware_sort = self.set_if_null(args.get("hardwaresort", default_sort_field), default_sort_field)
        self. __hardware_sort_dir = self.set_if_null(args.get("hardwaresortdir", default_sort_direction),
                                                     default_sort_direction)

    def __get_games(self):        
        get_games_interactor = self.interactor_factory.create("GetGamesInteractor")

        p = GetGamesInteractorParams()
        p.number_of_games = self.__config.get("front-page-games")
        p.sort_field = self.__game_sort
        p.sort_direction = self.__game_sort_dir
        p.user_id = self.session.get_value("user_id")
        p.platform = None
        try:
            games = get_games_interactor.execute(p)
        except UnrecognisedFieldNameException:
            raise cherrypy.HTTPRedirect("/")
        return games

    def __get_hardware(self):
        get_hardware_list_interactor = self.interactor_factory.create("GetHardwareListInteractor")
        return get_hardware_list_interactor.execute(sort_field=self.__hardware_sort, 
                                                    sort_direction=self.__hardware_sort_dir, 
                                                    user_id=self.session.get_value("user_id"))


    def __count_games(self):
        count_games_interactor = self.interactor_factory.create("CountGamesInteractor")
        number_of_games = count_games_interactor.execute()
        return number_of_games
