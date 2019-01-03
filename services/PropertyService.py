import yaml

from Decorators import Singleton


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
    def load_properties(self, file):
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


@Singleton
class PropertyServiceSingleton:
    __instance = None

    def __init__(self):
        print("init...")
        self.properties = {}

    # get property
    def get_property(self, key):
        return self.properties[key]

    # load properties from file iterative
    def load_properties(self, file):
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


# parser dict recursive
def parser_dict(k, obj, props):
    if isinstance(obj, dict):
        for k1, v1 in obj.items():
            parser_dict(k + "." + k1, v1, props)
    else:
        props[k] = obj
