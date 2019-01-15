from json import JSONEncoder

import webapp2
from webapp2_extras import json

from model.Employe import Employee
from model.Person import Person


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Employee):
            return Employee.get_marshall(obj)
        else:
            if isinstance(obj, Person):
                return Person.get_marshall(obj)
        return super(MyJSONEncoder, self).default(obj)


class EmployeeResource(webapp2.RequestHandler):

    # @marshal_with(Person.get_marshall())
    # @logging
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        # self.response.
        em = Employee(name="Subclass")
        persons = [Person(name="Alan Gabriel", em=em), Person("Davila", em)]
        self.response.write(json.encode(persons, cls=MyJSONEncoder, sort_keys=True))


app = webapp2.WSGIApplication([
    ('/api/v1/addup', EmployeeResource),
    ], debug=True)

