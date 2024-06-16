from abc import ABC
from datetime import  datetime

class Animal(ABC):
    
    def __init__(self,name, type_animal, birth_date, commands=None):
        self.name = name
        self.type = type_animal
        self.birth_date = birth_date
        self.commands=None
        if not commands:
            self.commands=[]
        else: self.commands=list(commands)
        
        
    def __str__(self):
        year_age=(datetime.now()-self.birth_date).days//365
        #дописать возраст в днях, если разница меньше месяца
        return f"Тип: {self.type}; кличка: {self.name}; возраст: {year_age} лет; знает команды: {',  '.join(self.commands)}"
    def get_name(self):
        return self.name
    def get_commands(self):
        return self.commands
    def set_commands(self,value):
        if value not in self.commands:
            self.commands.append(value)   


