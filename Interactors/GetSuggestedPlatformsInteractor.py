from Interactors.Interactor import Interactor


class GetSuggestedPlatformsInteractor(Interactor):

    def __init__(self, suggested_platforms):
        super().__init__()
        self.__suggested_platforms=suggested_platforms

    def execute(self):
        result = []
        platforms = self.persistence.get_platforms()
        suggested_platforms = self.__suggested_platforms.get()

        for suggested_platform in suggested_platforms:
            found = False

            for platform in platforms:
                if suggested_platform.name == platform.name:
                    found = True
                    break

            if found:
                continue
            result.append(suggested_platform)

        return result
