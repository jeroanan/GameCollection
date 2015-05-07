# This file is part of Icarus.

# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

from copy import copy
from Game import Game
from Persistence.Exceptions.GameNotFoundException import GameNotFoundException


class ResultToGameMapper(object):
    # map a MongoDB result to an object of type Game

    def __init__(self, mongo_result):
        """Initialise the mapper
        :param mongo_result: A MongoDB result. The following fields
        can currently be mapped:
          * _id
          * _Game__title
          * _Game__platform
          * _Game__num_copies
          * _Game__num_boxed
          * _Game__num_manuals
          * _Game__notes
          * _Game__date_purchased
          * _Game__appproximate_date_purhcased"""
        self.__mongo_result = mongo_result

    def map(self):
        # Map a single MongoDB result to an object of type Game
        def map_field(mongo_field_name, mapped_field_name, game):
            g = copy(game)
            if mongo_field_name in self.__mongo_result:
                setattr(g, mapped_field_name, self.__mongo_result[mongo_field_name])
            return g
        
        if self.__mongo_result is None:
            raise GameNotFoundException

        mappings = {"_id": "id",
                    "_Game__title": "title",
                    "_Game__platform": "platform",
                    "_Game__num_copies": "num_copies",
                    "_Game__num_boxed": "num_boxed",
                    "_Game__num_manuals": "num_manuals",
                    "_Game__notes": "notes",
                    "_Game__date_purchased": "date_purchased",
                    "_Game__approximate_date_purchased": "approximate_date_purchased"}
                    
        mapped = Game()        
        for k in mappings:
            mapped = map_field(k, mappings[k], mapped)

        return mapped
