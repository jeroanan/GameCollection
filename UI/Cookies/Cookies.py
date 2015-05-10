import cherrypy

class Cookies(object):
    
    def set_cookie(self, key, value):
        cherrypy.response.cookie[key] = value
        cherrypy.response.cookie[key]['max-age'] = 3600

    def clear_cookie(self, key):
        cherrypy.response.cookie[key] = ""
        cherrypy.response.cookie[key]["expires"] = 0

    def renew_cookie(self, key):
        print(key in cherrypy.request.cookie[key])
