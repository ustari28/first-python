import json

from flask_restful import fields


class Employee(object):
    def __init__(self, name):
        self.name = name
        self.years_old = 0
        self.profession = ""

    @staticmethod
    def get_marshall():
        return {
            'name': fields.String,
            'years_old': fields.Integer
        }
