class Game(object):

    def __init__(self):
        self.__id = ""
        self.__title = ""
        self.__platform = ""
        self.__num_copies = 0
        self.__num_boxed = 0
        self.__num_manuals = 0
        self.__notes = ""
        self.__date_purchased = ""
        self.__approximate_date_purchased = False

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    @property
    def num_copies(self):
        return self.__num_copies

    @num_copies.setter
    def num_copies(self, value):
        self.__num_copies = value

    @property
    def num_boxed(self):
        return self.__num_boxed

    @num_boxed.setter
    def num_boxed(self, value):
        self.__num_boxed = value

    @property
    def num_manuals(self):
        return self.__num_manuals

    @num_manuals.setter
    def num_manuals(self, value):
        self.__num_manuals = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value

    @property
    def date_purchased(self):
        return self.__date_purchased

    @date_purchased.setter
    def date_purchased(self, value):
        self.__date_purchased = value

    @property
    def approximate_date_purchased(self):
        return self.__approximate_date_purchased

    @approximate_date_purchased.setter
    def approximate_date_purchased(self, value):
        self.__approximate_date_purchased = value

    def __eq__(self, other):
        return (self.title == other.title and self.platform == other.platform and self.num_copies == other.num_copies
                and self.num_boxed == other.num_boxed and self.num_manuals == other.num_manuals and
                self.notes == other.notes)