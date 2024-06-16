from Animal import Animal
class PackPets(Animal):
    def __repr__(self):
        return self.__bases__[0].__name__

class Horses(PackPets):
    pass

class Donkeys(PackPets):
    pass

class Camels(PackPets):
    pass