from collections.abc import abc
from datetime import date, datetime
class Animal(ABC):
    def __init__(self, name, type, birth_date, commands=[]) -> None:
        self.name = name
        self.type = type
        data=birth_date.split('.') # введите дату в формате дд.мм.ГГГГ
        self.birth_date = date(int(data[2]),int(data[1]),int(data[0]))
        self.commands=list(commands)
    @abstractmethod
    def __str__(self):
        year_age=(datetime.now()-self.birth_date).days()//365 
        #дописать возраст в днях, если разница меньше месяца
        return f"Тип: {self.type}; кличка: {self.name}; возраст: {year_age} years; знает команды: {',  '.join(self.commands)}"
    def __add__(self, value):
        pass
    def __iadd__(self,value):
        pass
        


