from Animal import Animal


class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.tricks = []
        self.set_specie("Dog")

    def add_trick(self, trick):
        self.tricks.append(trick)
