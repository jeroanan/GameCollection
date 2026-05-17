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

import cherrypy

class Cookies(object):
    
    def set_cookie(self, key, value):
        cherrypy.response.cookie[key] = value
        cherrypy.response.cookie[key]['max-age'] = 3600

    def clear_cookie(self, key):
        cherrypy.response.cookie[key] = ""
        cherrypy.response.cookie[key]["expires"] = 0

    def renew_cookie(self, key):
        if key in cherrypy.request.cookie:
            cherrypy.response.cookie[key] = cherrypy.request.cookie[key].coded_value
            cherrypy.response.cookie[key]["expires"] = 3600
