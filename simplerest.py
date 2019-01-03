from datetime import datetime

from flask import Flask
from flask_restful import Api

from Decorators import security

from services.EmplyeeResource import EmployeeResource
from services.PropertyService import PropertyServiceSingleton

"""
Start a new Application
"""

app = Flask(__name__)
api = Api(app)
api.decorators = [security("enabled")]
print(datetime.now())
prop_service = PropertyServiceSingleton()
prop_service.load()
api.add_resource(EmployeeResource, "/api/v1/employees", )
print("{} prop {}".format(datetime.now(), prop_service.get_property("darwin.security.mode")))
