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

import json

import cherrypy

import UI.Handlers.AuthenticatedHandler as ah


class GetExportHandler(ah.AuthenticatedHandler):

    def get_page(self, params):
        super().get_page(params)
        p = params['data[]']

        if not isinstance(p, list):
            p = p.split(',')
        
        interactor = self.interactor_factory.create('ExportCollectionInteractor')
        collection_data = interactor.execute(p, self.session.get_value("user_id"))

        result = {}
        for k, v in collection_data.items():
            values = []
            for g in v:
                values.append(json.loads(g.to_json()))
            result[k] = values

        cherrypy.response.headers['Content-Type'] = 'application/json'
        cherrypy.response.headers['Content-Disposition'] = 'attachment; filename="icarus_collection.json"'
        return json.dumps(result).encode('utf-8')

