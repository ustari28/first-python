from flask_restful import fields

from model.Employe import Employee


class Person(object):

    def __init__(self, name, em: Employee):
        self.name = name
        self.em = em

# Get_marshall returns the list of fields to encode
    @staticmethod
    def get_marshall():
        return {
            'name': fields.String,
            'em': fields.Nested(Employee.get_marshall())
        }
