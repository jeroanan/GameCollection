# Copyright (c) 20115 David Wilson
# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

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

    @staticmethod
    def from_mongo_result(mongo_result):
        """Initialises an instance of Game from a MongoDB result.
        :param mongo_result: A MongoDB result as a dictionary with the following keys:
           * _id
           * __Game__title
           * _Game__platform
           * _Game__num_copies 
           * _Game__num_boxed
           * _Game__num_manuals
           * _Game__notes
           * _Game__date_purchased
           * _Game__approximate_date_purchased
        :returns: An instance of Game with its properties set. Missing keys from mongo_result will have their property 
                  set as the default.
        """
        g = Game()
        g.id = mongo_result.get("_id", g.id)
        g.title = mongo_result.get("_Game__title", g.title)
        g.platform = mongo_result.get("_Game__platform", g.platform)
        g.num_copies = mongo_result.get("_Game__num_copies", g.num_copies)
        g.num_boxed = mongo_result.get("_Game__num_boxed", g.num_boxed)
        g.num_manuals = mongo_result.get("_Game__num_manuals", g.num_manuals)
        g.notes = mongo_result.get("_Game__notes", g.notes)
        g.date_purchased = mongo_result.get("_Game__date_purchased", g.date_purchased)
        g.approximate_date_purchased = mongo_result.get("_Game__approximate_date_purchased", 
                                                        g.approximate_date_purchased)
        return g

    @staticmethod
    def from_dict(d):
        """Initialises an instance of Game from a dictionary.
        :param d: A dictionary with the following keys:
                     * title
                     * num_copies
                     * num_boxed
                     * num_manuals
                     * platform
                     * notes
        :returns: An instance of Game with its properties set. Missing keys from d will have their property
                  set as the default."""
        g = Game()
        g.title = d.get("title", g.title)
        g.num_copies = d.get("numcopies", g.num_copies)
        g.num_boxed = d.get("numboxed", g.num_boxed)
        g.num_manuals = d.get("nummanuals", g.num_manuals)
        g.platform = d.get("platform", g.platform)
        g.notes = d.get("notes", g.notes)
        return g
