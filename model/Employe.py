import json


class Employee:
    def __init__(self, name):
        self.name = name
        self.years_old = 0
        self.profession = ""

    def __repr__(self):
        return vars(self)
