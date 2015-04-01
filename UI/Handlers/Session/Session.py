import cherrypy


class Session(object):

    def set_value(self, key, value):
        cherrypy.session[key] = value

    def get_value(self, key):
        return cherrypy.session[key]
