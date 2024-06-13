from abc import ABC, abstractmethod
from datetime import date, datetime

class Animal(ABC):
    
    def __init__(self, name, type_animal, birth_date, commands=None):
        self.name = name
        self.type = type_animal
        self.birth_date = birth_date
        if commands is None:
            self.commands=[]
        else:
            self.commands=list(commands)
        
        
    @abstractmethod
    def __str__(self):
        year_age=(datetime.now()-self.birth_date).days()//365 
        #дописать возраст в днях, если разница меньше месяца
        return f"Тип: {self.type}; кличка: {self.name}; возраст: {year_age} лет; знает команды: {',  '.join(self.commands)}"
    
    def __add__(self, value):
        pass 
    
    def __iadd__(self,value):
        pass
        

