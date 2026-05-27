"""The Add Game page""" 

from ui.handlers.authenticated_handler import AuthenticatedHandler


class AddGameHandler(AuthenticatedHandler):
    """The Add Game page""" 

    def get_page(self, args: dict[str, str]) -> str:
        """Get the Add Game page.
        :param args: Page args (an empty dictionary in this case)
        :returns: The Add Game page, rendered as HTML
        """
        super().get_page(args)

        def get_from_interactor(interactor_type: str) -> list[str]:
            interactor = self.interactor_factory.create(interactor_type)
            return interactor.execute()

        platforms = get_from_interactor("GetPlatformsInteractor")
        genres = get_from_interactor("GetGenresInteractor")
        return self.renderer.render(
            "addgame.html",
            title="Add Game",
            platforms=platforms,
            genres=genres)
