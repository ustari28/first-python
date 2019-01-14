class Employee(object):
    def __init__(self, name):
        self.name = name
        self.years_old = 0
        self.profession = ""

    @staticmethod
    def get_marshall(obj):
        return {
            'name': obj.name,
            'years_old': obj.years_old
        }
