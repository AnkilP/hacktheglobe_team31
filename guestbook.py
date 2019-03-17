#!/usr/bin/env python

# Copyright 2016 Google Inc.
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

# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity.

    We use guestbook_name as the key.
    """
    return ndb.Key('Guestbook', guestbook_name)


# [START greeting]
class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    prefix = ndb.StringProperty(indexed=True)
    country_residence = ndb.StringProperty(indexed=True)
    country_citizenship = ndb.StringProperty(indexed=True)
    native_language = ndb.StringProperty(indexed=True)
    level_of_english = ndb.IntegerProperty(indexed=True)
    level_of_french = ndb.IntegerProperty(indexed=True)
    can_avail = ndb.IntegerProperty(indexed=True)
    education_level =  ndb.IntegerProperty(indexed=True)
    institution = ndb.StringProperty(indexed=True)
    eng_program = ndb.IntegerProperty(indexed=True)
    education_level_2 = ndb.IntegerProperty(indexed=True)
    institution2 = ndb.StringProperty(indexed=True)
    eng_program2 = ndb.IntegerProperty(indexed=True)
    work_exp = ndb.StringProperty(indexed=True)
    start_date = ndb.DateProperty(indexed=True)
    end_date = ndb.DateProperty(indexed=True)
    role = ndb.StringProperty(indexed=True)
    employer = ndb.StringProperty(indexed=True)
    work_location = ndb.StringProperty(indexed=True)
    industry = ndb.IntegerProperty(indexed=True)
    achievements = ndb.StringProperty(indexed=True)
    work_exp2 = ndb.StringProperty(indexed=True)
    start_date2 = ndb.DateProperty(indexed=True)
    end_date2 = ndb.DateProperty(indexed=True)
    role2 = ndb.StringProperty(indexed=True)
    employer2 = ndb.StringProperty(indexed=True)
    work_location2 = ndb.StringProperty(indexed=True)
    industry2 = ndb.IntegerProperty(indexed=True)
    achievements2 = ndb.StringProperty(indexed=True)
    work_exp3 = ndb.StringProperty(indexed=True)
    start_date3 = ndb.DateProperty(indexed=True)
    end_date3 = ndb.DateProperty(indexed=True)
    role3 = ndb.StringProperty(indexed=True)
    employer3 = ndb.StringProperty(indexed=True)
    work_location3 = ndb.StringProperty(indexed=True)
    industry3 = ndb.IntegerProperty(indexed=True)
    achievements3 = ndb.StringProperty(indexed=True)
    skills = ndb.IntegerProperty(indexed=True)
    skills_resp = ndb.StringProperty(indexed=True)

class Greeting(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
# [END greeting]


# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
# [END main_page]


# [START guestbook]
class Guestbook(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

        greeting.prefix = self.request.get('prefix')
        greeting.country_residence = self.request.get('country_residence')
        greeting.country_citizenship = self.request.get('country_citizenship')
        greeting.native_language = self.request.get('native_language')
        greeting.level_of_english = self.request.get('level_of_english')
        greeting.level_of_french = self.request.get('level_of_french')
        greeting.can_avail = self.request.get('can_avail')
        greeting.education_level =  self.request.get('education_level')
        greeting.institution = self.request.get('institution')
        greeting.eng_program = self.request.get('eng_program')
        greeting.education_level_2 = self.request.get('education_level_2')
        greeting.institution2 = self.request.get('institution2')
        greeting.eng_program2 = self.request.get('eng_program2')
        greeting.work_exp = self.request.get('work_exp')
        greeting.start_date = self.request.get('start_date')
        greeting.end_date = self.request.get('end_date')
        greeting.role = self.request.get('role')
        greeting.employer = self.request.get('employer')
        greeting.work_location = self.request.get('work_location')
        greeting.industry = self.request.get('industry')
        greeting.achievements = self.request.get('achievements')
        greeting.work_exp2 = self.request.get('work_exp2')
        greeting.start_date2 = self.request.get('start_date2')
        greeting.end_date2 = self.request.get('end_date2')
        greeting.role2 = self.request.get('role2')
        greeting.employer2 = self.request.get('employer2')
        greeting.work_location2 = self.request.get('work_location2')
        greeting.industry2 = self.request.get('industry2')
        greeting.achievements2 = self.request.get('achievements2')
        greeting.work_exp3 = self.request.get('work_exp3')
        greeting.start_date3 = self.request.get('start_date3')
        greeting.end_date3 = self.request.get('end_date3')
        greeting.role3 = self.request.get('role3')
        greeting.employer3 = self.request.get('employer3')
        greeting.work_location3 = self.request.get('work_location3')
        greeting.industry3 = self.request.get('industry3')
        greeting.achievements3 = self.request.get('achievements3')
        greeting.skills = self.request.get('skills')
        greeting.skills_resp = self.request.get('skills_resp')
        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))
# [END guestbook]


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
# [END app]
