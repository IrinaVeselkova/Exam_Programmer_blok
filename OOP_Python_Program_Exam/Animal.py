from abc import ABC
from datetime import  datetime

class Animal(ABC):
    
    def __init__(self,name, type_animal, birth_date, commands=None):
        self.name = name
        self.type = type_animal
        self.birth_date = birth_date
        if not commands:
            self.commands=[]
        else: self.commands=list(commands)
        
        
    def __str__(self):
        year_age=(datetime.now()-self.birth_date).days//365
        #дописать возраст в днях, если разница меньше месяца
        return f"Тип: {self.type}; кличка: {self.name}; возраст: {year_age} лет; знает команды: {',  '.join(self.commands)}"
    
           


