import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {"name": "CSSI NYC",
                        "food": "Pizza",
                        "music": "Jazz"}
        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render(template_vars))

class CountHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1, 21):
          self.response.write('Hello %d <br>' % i)

app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
  ('/count', CountHandler),
  ('/', CountHandler)
], debug=True)
