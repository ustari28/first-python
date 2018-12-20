class Animal:

    def __init__(self, name):
        self.name = name
        self.size = 0
        self.__specie = ""
        self.source = ""

    def set_size(self, size):
        self.size = size

    def set_source(self, source):
        self.source = source

    def set_specie(self, specie):
        self.__specie = specie

    def get_specie(self):
        return self.__specie
