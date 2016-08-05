#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class Get1Handler(webapp2.RequestHandler):
    def get(self):
        self.response.write('OK')

class Post1Handler(webapp2.RequestHandler):
    def post(self):
        value = self.request.get('textbox')
        self.response.write('Posted' + value)


    def get(self):
        self.response.write('gotten')

class GetFormHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html>'
                            '<form method=POST action="post_1">'
                            '<input type="text" name="textbox"></input>'
                            '<input type="submit"></input>'
                            '</form>'
                            '</html>')



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/get_1', Get1Handler),
    ('/get_form', GetFormHandler ),
    ('/post_1', Post1Handler),
], debug=True)
