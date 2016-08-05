import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__), 'templates')


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pig-input.html')
        self.response.write(template.render())

    def pig-latin:
        pigword = ''
        str.split('',1)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ], debug=True)
