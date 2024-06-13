from collections.abc import abc
class Animal(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def __str__(self):
        pass
    def __add__(self, value):
        pass
        
        
class Pets(Animal):
    pass

class PackPets(Animal):
    pass

class Cats(Pets):
    pass

class Cats(Pets):
    pass

class Cats(Pets):
    pass
