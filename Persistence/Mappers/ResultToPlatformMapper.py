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

from Platform import Platform


class ResultToPlatformMapper(object):

    def __init__(self, mongo_result):
        self.__mongo_result = mongo_result

    def map(self):

        mappings = {"_id": "id",
                    "_Platform__name": "name",
                    "_Platform__description": "description"}
        
        platform = Platform()
        for k in mappings:
            if k in self.__mongo_result:
                setattr(platform, mappings[k], self.__mongo_result[k])

        return platform
