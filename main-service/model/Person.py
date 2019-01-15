from model.Employe import Employee


class Person(object):

    def __init__(self, name, em):
        self.name = name
        self.em = em

    # Get_marshall returns the list of fields to encode
    @staticmethod
    def get_marshall(obj):
        return {
            'name': obj.name,
            'em': Employee.get_marshall(obj.em)
        }
