import cherrypy


class Session(object):

    def set_value(self, key, value):
        cherrypy.session[key] = value

    def get_value(self, key):
        if key in cherrypy.session:
            return cherrypy.session[key]
        return ""
