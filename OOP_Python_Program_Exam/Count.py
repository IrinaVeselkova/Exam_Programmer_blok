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
    def __iter__ (self):
        yield from self.reestr_list
    def __len__(self):
        return len(self.reestr_list)