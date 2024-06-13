from PackPets import *
from Pets import *

class Count:
    def __init__(self):
        self.reestr_list=[]
        
    def add(self, value):
        if isinstance(value, (Cats, Dogs, Hamsters, Horses, Donkeys, Camels)):
            self.reestr_list.append(value)
        else:
            return NotImplemented