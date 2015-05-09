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

from Hardware import Hardware
from Persistence.Exceptions.HardwareNotFoundException import HardwareNotFoundException


class ResultToHardwareMapper(object):
    # Maps a single MongoDB result row to an object of type Hardware

    def __init__(self, mongo_result):
        """Initialise the mapper
        :param mongo_result: A MongoDB result. The following fields
        can currently be mapped:
          * _id
          * _Hardware__name
          * _Hardware__num_owned
          * _Hardware__num_boxed
          * _Hardware__notes
        Any of these fields that are not included will not be mapped and
        be returned as their default values in the Hardware object."""

        if mongo_result is None:
                raise HardwareNotFoundException()
        self.__mongo_result = mongo_result

    def map(self):    
        """Perform mapping on the MongoDB result set passed in at object construction
        :returns: An object of type Hardware containing the mapped result."""
        mappings = {
            "_id": "id",
            "_Hardware__name": "name",
            "_Hardware__platform": "platform",
            "_Hardware__num_owned": "num_owned",
            "_Hardware__num_boxed": "num_boxed",
            "_Hardware__notes": "notes"
        }

        hardware = Hardware()

        for k in mappings:
            if k in self.__mongo_result:
                setattr(hardware, mappings[k], self.__mongo_result[k])

        return hardware
