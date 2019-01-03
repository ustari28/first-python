from datetime import datetime

from flask import Flask
from flask_restful import Api
from pipenv.vendor import requests
from pipenv.vendor.requests import RequestException

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
try:
    cloud = requests.get('http://localhost:8888/mysmartercv/develop/master')
    if cloud.status_code != 200:
        print("Some error ocurred while we requested configuration to configuration service", cloud.status_code)
        exit(1)
    remote = cloud.json()
    print(datetime.now())
    print(remote['propertySources'][0]['source']['test.app.name'])
    api.add_resource(EmployeeResource, "/api/v1/employees", )

    PropertyServiceSingleton().load_properties("resources/bootstrap.yml")
    PropertyServiceSingleton().load_properties("resources/bootstrap.yml")

except RequestException as er:
    print(er.args[0])
    exit(1)
