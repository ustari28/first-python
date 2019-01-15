import requests
import yaml
from requests import RequestException

from Decorators import Singleton


# Property service with internal singleton method
class PropertyService:
    __instance = None

    def __init__(self):
        print("init...")
        self.properties = {}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("creating new instance...")
            cls.__instance = super(PropertyService, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    # get property
    def get_property(self, key):
        return self.properties[key]

    # load properties from file iterative
    def load_properties(self, file="bootstrap.yml"):
        stream = open(file, "r")
        docs = yaml.load_all(stream)
        props = {}
        for doc in docs:
            _exists = False
            for k, v in doc.items():
                if not _exists:
                    if isinstance(v, dict):
                        _exists = True
                props[k] = v
            while _exists:
                _exists = False
                temp = {}
                for k1, v1 in props.items():
                    if isinstance(v1, dict):
                        for a, b in v1.items():
                            vvalue = k1 + "." + a
                            if not _exists:
                                if isinstance(b, dict):
                                    _exists = True
                            temp[vvalue] = b
                    else:
                        temp[k1] = v1
                props = temp.copy()
        self.properties = props.copy()
        for k1, v1 in self.properties.items():
            print("key : {0} value: {1}".format(k1, v1))
        stream.close()


# Property service with singleton decorator
@Singleton
class PropertyServiceSingleton:
    __instance = None

    def __init__(self):
        print("init...")
        self.properties = {}

    # get property
    def get_property(self, key):
        return self.properties[key]

    def load(self):
        self.__load_properties("resources/bootstrap.yml")
        self.__load_remote_properties()

    # load properties from file iterative
    def __load_properties(self, file):
        stream = open(file, "r")
        docs = yaml.load_all(stream)
        props = {}
        for doc in docs:
            _exists = False
            for k, v in doc.items():
                if not _exists:
                    if isinstance(v, dict):
                        _exists = True
                props[k] = v
            while _exists:
                _exists = False
                temp = {}
                for k1, v1 in props.items():
                    if isinstance(v1, dict):
                        for a, b in v1.items():
                            vvalue = k1 + "." + a
                            if not _exists:
                                if isinstance(b, dict):
                                    _exists = True
                            temp[vvalue] = b
                    else:
                        temp[k1] = v1
                props = temp.copy()
        self.properties = props.copy()
        for k1, v1 in self.properties.items():
            print("key : {0} value: {1}".format(k1, v1))
        stream.close()

    # load remote properties from cloud server configuration
    def __load_remote_properties(self):
        try:
            cloud = requests.get('http://localhost:8888/mysmartercv/develop/master')
            if cloud.status_code != 200:
                print("Some error ocurred while we requested configuration to configuration service", cloud.status_code)
            remote = cloud.json()
            props = remote['propertySources'][0]['source']
            for k, v in props.items():
                self.properties[k] = v
        except RequestException as er:
            print(er.args[0])


# parser dict recursive
def parser_dict(k, obj, props):
    if isinstance(obj, dict):
        for k1, v1 in obj.items():
            parser_dict(k + "." + k1, v1, props)
    else:
        props[k] = obj
