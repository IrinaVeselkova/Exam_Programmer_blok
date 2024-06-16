from PackPets import *
from Pets import *

class AnimalRegister:
    def __init__(self):
        self.reestr_list=[]    
    def add(self, data):
        match data[1]:
                case "верблюд":
                    self.reestr_list.append(Camels(data[0],data[1],data[2],data[3]))                    
                case 'кот':
                    self.reestr_list.append(Cats(data[0],data[1],data[2],data[3]))                    
                case "лошадь":
                    self.reestr_list.append(Horses(data[0],data[1],data[2],data[3]))                    
                case "хомяк":
                    self.reestr_list.append(Hamsters(data[0],data[1],data[2],data[3]))                    
                case "собака":
                    self.reestr_list.append(Dogs(data[0],data[1],data[2],data[3]))
                case "осел":
                    self.reestr_list.append(Donkeys(data[0],data[1],data[2],data[3])) 
    def __iter__ (self):
        yield from self.reestr_list
    def __len__(self):
        return len(self.reestr_list)
    
        
            
        