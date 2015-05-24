# Copyright (c) David Wilson 2015
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

import unittest

from User import User


class TestUser(unittest.TestCase):

    def test_from_dict_does_mapping(self):
        """Mapping from a dictionary to a User object performs correct mappings"""
        d = {"userid": "user_id",
             "password": "pw",
             "id": "1234"}
        u = User.from_dict(d)
        self.assertEqual(d["userid"], u.user_id)
        self.assertEqual(d["password"], u.password)
        self.assertEqual(d["id"], u.id)

    def test_from_mongo_result_does_mapping(self):
        """Mongo result maps to User object"""
        ud = {"_id": "id",
              "_User__user_id": "user_id",
              "_User__password": "password"}
        u = User.from_mongo_result(ud)
        self.assertEqual(ud["_id"], u.id)
        self.assertEqual(ud["_User__user_id"], u.user_id)
        self.assertEqual(ud["_User__password"], u.password)
