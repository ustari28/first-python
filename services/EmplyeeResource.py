from flask import request
from flask_restful import Resource, marshal_with, reqparse

from Decorators import logging
from model.Employe import Employee
from model.Person import Person


class EmployeeResource(Resource):

    @marshal_with(Person.get_marshall())
    @logging
    def get(self):
        print(request.method)
        # conn = db_connect.connect() # connect to database
        # query = conn.execute("select * from employees") # This line performs query and returns json result
        # return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        em = Employee(name="Subclass")
        persons = [Person(name="Alan Gabriel", em=em), Person("Dávila", em)]
        return persons, 200

    @marshal_with(Person.get_marshall())
    def post(self):
        print(request.method)
        # conn = db_connect.connect() # connect to database
        # query = conn.execute("select * from employees") # This line performs query and returns json result
        # return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        em = Employee(name="Subclass")
        persons = [Person(name="Alan Gabriel", em=em), Person("Dávila", em)]
        return persons, 200
