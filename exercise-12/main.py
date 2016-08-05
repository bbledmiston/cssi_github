import jinja2
import os
from google.appengine.api import users
import webapp2
from google.appengine.ext import ndb
import logging

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        self.response.out.write('%s' % greeting)
        template = jinja_environment.get_template('templates/input_order.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('templates/output_order.html')
        pizza_order = {
          'crust_answer': self.request.get('crust'),
          'size_answer': self.request.get('size'),
          'sauce_answer': self.request.get('sauce'),
          'cheese_answer': self.request.get('cheese'),
          'topings_answer': self.request.get('topings')}
          pizza_order = {
            'crust_answer': crust_value,
            'size_answer': size_value,
            'sauce_answer': sauce_value,
            'cheese_answer': cheese_value,
            'topings_anser': topings_value
          }
          order_record = Order(crust=crust_value, size=size_value, sauce=sauce_value, cheese=cheese_value, topings=topings_value
          )
          order_record.put()
          self.response.write(template.render(pizza_order))

class Order(ndb.Model):
    crust_answer = ndb.StringProperty(required=True)
    size_answer = ndb.StringProperty(required=True)
    sauce_answer = ndb.IntegerProperty(required=True)
    cheese_answer = ndb.IntegerProperty(required=True)
    topings_answer = ndb.IntegerProperty(required=True)


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
