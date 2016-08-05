import jinja2
import os
from google.appengine.api import users
import webapp2
from google.appengine.ext import ndb


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Customer(ndb.Model):
    name = ndb.StringProperty(required=True)
    address = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    pizza_key = ndb.KeyProperty(kind='Order')

class Order(ndb.Model):
    crust = ndb.StringProperty(required=True)
    size = ndb.StringProperty(required=True)
    sauce = ndb.StringProperty(required=True)
    cheese = ndb.StringProperty(required=True)
    topings = ndb.StringProperty(required=True)
    time = ndb.IntegerProperty(required=True)
    price = ndb.IntegerProperty(required=True)
    pizza_description = ndb.StringProperty(required=True)


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

        crust_value=self.request.get('crust')
        size_value=self.request.get('size')
        sauce_value=self.request.get('sauce')
        cheese_value=self.request.get('cheese')
        topings_value=self.request.get('topings')
        name_value=self.request.get('name')
        address_value=self.request.get('address')
        phone_value=self.request.get('phone')
        order_record = Order(crust=crust_value,size=size_value, sauce=sauce_value, cheese=cheese_value, topings=topings_value, time=12, pizza_description="good", price=10)
        key = order_record.put()

        pizza_order = {
            'crust_answer': crust_value,
            'size_answer': size_value,
            'sauce_answer': sauce_value,
            'cheese_answer': cheese_value,
            'topings_answer': topings_value,
            'order_number' : key.id()
          }
        customer_record = Customer(name=name_value, address=address_value, phone=phone_value, pizza_key=order_record.put())
        key = customer_record.put()

    #    pizza_description = ['crust_answer' + 'size_answer' + 'sauce_answer' + 'cheese_answer' + 'topings_answer']



        self.response.write(template.render(pizza_order))
        self.response.write(key.id())




app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
