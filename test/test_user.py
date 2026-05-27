"""Unit tests for the User class"""
# Copyright (c) David Wilson 2015, 2026
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

import icarus_user as u


class TestUser(unittest.TestCase):
    """Unit tests for the User class"""

    def test_from_dict_does_mapping(self) -> None:
        """Mapping from a dictionary to a User object performs correct mappings"""
        d = {"userid": "user_id",
             "password": "pw",
             "id": "1234"}
        user = u.User.from_dict(d)
        self.assertEqual(d["userid"], user.user_id)
        self.assertEqual(d["password"], user.password)
        self.assertEqual(d["id"], user.id)
