class Handler(object):

    def __init__(self, interactor_factory, renderer):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer

    @property
    def interactor_factory(self):
        return self.__interactor_factory

    @property
    def renderer(self):
        return self.__renderer

    def set_if_null(self, variable, value):
        if variable is None:
            return value
        return variable

