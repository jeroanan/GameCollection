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

import functools as ft
import json


class Game(object):
    """Represents a game"""

    def __init__(self):
        """Initialise object state"""
        self.__id = ""
        self.__genre = ""
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
        """Get game id"""
        return self.__id

    @id.setter
    def id(self, value):
        """Set game id"""
        self.__id = value

    @property
    def genre(self):
        """Get game genre"""
        return self.__genre

    @genre.setter
    def genre(self, val):
        """Set game genre"""
        self.__genre = val

    @property
    def title(self):
        """Get game title"""
        return self.__title

    @title.setter
    def title(self, value):
        """Set game title"""
        self.__title = value

    @property
    def platform(self):
        """Get game platform"""
        return self.__platform

    @platform.setter
    def platform(self, value):
        """Set game platform"""
        self.__platform = value

    @property
    def num_copies(self):
        """Get number of copies of the game owned"""
        return self.__num_copies

    @num_copies.setter
    def num_copies(self, value):
        """Set number of copies of the game owned"""
        self.__num_copies = value

    @property
    def num_boxed(self):
        """Get number of copies of the game boxed"""
        return self.__num_boxed

    @num_boxed.setter
    def num_boxed(self, value):
        """Set number of copies of the game boxed"""
        self.__num_boxed = value

    @property
    def num_manuals(self):
        """Get number of manuals owned for the game"""
        return self.__num_manuals

    @num_manuals.setter
    def num_manuals(self, value):
        """Set number of manuals owned for the game"""
        self.__num_manuals = value

    @property
    def notes(self):
        """Get notes held against the game"""
        return self.__notes

    @notes.setter
    def notes(self, value):
        """Set notes held against the game"""
        self.__notes = value

    @property
    def date_purchased(self):
        """Get the date the game was purchased on"""
        return self.__date_purchased

    @date_purchased.setter
    def date_purchased(self, value):
        """Set the date the game was purchased on"""
        self.__date_purchased = value

    @property
    def approximate_date_purchased(self):
        """Get whether the game's purchase date is approximate"""
        return self.__approximate_date_purchased

    @approximate_date_purchased.setter
    def approximate_date_purchased(self, value):
        """Set whether the game's purchase date is approximate"""
        self.__approximate_date_purchased = value

    def __eq__(self, other):
        """Test whether this instance of Game is equal to another
        This happens by comparing the following properties:
           * title
           * platform
           * num_copies
           * num_boxed
           * num_manuals
           * notes
        :returns: True if this instance of Game is equal to other, otherwise False
        """
        return (self.title == other.title and self.platform == other.platform and
                self.num_copies == other.num_copies and self.num_boxed == other.num_boxed and
                self.num_manuals == other.num_manuals and self.notes == other.notes)

    @staticmethod
    def from_mongo_result(mongo_result):
        """Initialises an instance of Game from a MongoDB result.
        :param mongo_result: A MongoDB result as a dictionary. 
                             See mappings below for details on expected keys.
        :returns: An instance of Game with its properties set.
                  Missing keys from mongo_result will have their property set as the default.
        """

        # game.attr, mongo_result.key
        mappings = {"genre": "_Game__genre",
                    "id": "_id",
                    "title":"_Game__title",
                    "platform": "_Game__platform",
                    "num_copies": "_Game__num_copies",
                    "num_boxed": "_Game__num_boxed",
                    "num_manuals": "_Game__num_manuals",
                    "notes": "_Game__notes",
                    "date_purchased": "_Game__date_purchased",
                    "approximate_date_purchased": "_Game__approximate_date_purchased"}

        return Game._from_dict(mongo_result, mappings)    

    @staticmethod
    def from_dict(dictionary):
        """Initialises an instance of Game from a dictionary.
        
        :param dictionary: A dictionary.  See mapping below for details on expected keys.
        :returns: An instance of Game with its properties set. Missing keys from d will have their
                  property set as the default."""

        # game.attr, dictionary.key
        mappings = {"id": "id",
                    "date_purchased": "datepurchased",
                    "genre": "genre",
                    "title": "title",
                    "num_copies": "numcopies",
                    "num_boxed": "numboxed",
                    "num_manuals": "nummanuals",
                    "platform": "platform",
                    "notes": "notes"}
                   
        return Game._from_dict(dictionary, mappings)

    @staticmethod
    def _from_dict(dictionary, mappings):
        game = Game()

        set_attr = ft.partial(setattr, game)
        get_attr = ft.partial(getattr, game)
        dict_get = lambda x: dictionary.get(x[0], get_attr(x[1]))

        list(map(lambda m: set_attr(m, dict_get((mappings[m], m))), mappings))
        return game

    def to_json(self):
        attrs = ["date_purchased", "genre", "title", "num_copies", "num_boxed", "num_manuals", "platform", "notes"]
        result = {}

        result["id"] = str(self.id)

        for a in attrs:
            result[a] = getattr(self, a)
        
        return json.dumps(result)
