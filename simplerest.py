from flask import Flask, request
from flask_restful import Resource, Api

from services.EmplyeeResource import EmployeeResource

"""
Start a new Application
"""
app = Flask(__name__)
api = Api(app)

api.add_resource(EmployeeResource, "/api/v1/employees", )
