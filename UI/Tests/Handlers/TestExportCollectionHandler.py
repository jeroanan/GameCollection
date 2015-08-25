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
from unittest.mock import Mock

import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.ExportCollectionHandler as ech
import UI.Handlers.Session.Session as sess
import UI.TemplateRenderer as tr


class TestExportCollectionHandler(unittest.TestCase):
    
    def setUp(self):
        self.__renderer = Mock(tr.TemplateRenderer)
        self.__target = ech.ExportCollectionHandler(None, self.__renderer)
        self.__target.session = Mock(sess.Session)

    def test_is_instance_of_authenticated_handler(self):        
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        self.__target.get_page(None)
        self.__renderer.render.assert_called_with('exportcollection.html', title='Export Collection')
