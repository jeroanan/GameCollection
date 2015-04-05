from UI.Handlers.Handler import Handler


class PlatformsHandler(Handler):

    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()
        return self.renderer.render("platforms.html", title="Manage Platforms", platforms=(self.__get_platforms()),
                                    suggested_platforms=(self.__get_suggested_platforms()))

    def __get_platforms(self):
        return self.__get_interactor_data("GetPlatformsInteractor")

    def __get_suggested_platforms(self):
        return self.__get_interactor_data("GetSuggestedPlatformsInteractor")

    def __get_interactor_data(self, interactor_name):
        interactor = self.interactor_factory.create(interactor_name)
        data = interactor.execute()
        return data
