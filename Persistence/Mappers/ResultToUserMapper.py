# Copyright (c) 2015 David Wilson
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

from Persistence.Mappers.Mapping import do_mapping
from User import User

class ResultToUserMapper(object):
    # Maps a Mongo Result to an object of type User

    def __init__(self, mongo_result):
        """Initialise the mapper
        :param mongo_result: A MongoDB result. The following fields
        can currently be mapped:
          * _id
          * _User__user_id
          * _User__password
        """
        self.__mongo_result = mongo_result
    
    def map(self):
        # Maps a Mongo Result to an object of type User
        if self.__mongo_result is None:
            return User()

        mappings = {"_id": "id",
                    "_User__user_id": "user_id",
                    "_User__password": "password"}
        return do_mapping(mappings, self.__mongo_result, User())

