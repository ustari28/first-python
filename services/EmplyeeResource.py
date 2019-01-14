import webapp2
from flask import request
from flask_restful import Resource, marshal_with

from Decorators import logging
from model.Employe import Employee
from model.Person import Person


class EmployeeResource(webapp2.RequestHandler):

    @marshal_with(Person.get_marshall())
    @logging
    def get(self):
        em = Employee(name="Subclass")
        persons = [Person(name="Alan Gabriel", em=em), Person("Dávila", em)]
        return persons, 200

    @marshal_with(Person.get_marshall())
    def post(self):
        em = Employee(name="Subclass")
        persons = [Person(name="Alan Gabriel", em=em), Person("Dávila", em)]
        return persons, 200
