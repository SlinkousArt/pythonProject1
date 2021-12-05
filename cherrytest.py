import cherrypy
import os


var1 = "sample text"

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <body>
            """, var1, """
          </body>
        </html>"""


conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'assets'
        }
    }
cherrypy.quickstart(HelloWorld())

print(os.path.abspath(os.getcwd()))
