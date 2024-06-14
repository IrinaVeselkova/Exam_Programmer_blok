from Count import Count
from Pets import *
from PackPets import *
from Functions import *

animals_registry=Count()
while True:
    match menu():
        case 1:
            data=for_one_menu()
            animals_registry.add(Cats(data[0],data[1],data[2],data[3]))
            print("Животное добавлено в реестр")
            if input("Перейти в меню? (Д/Н)").strip().lower() not in ('д', "y"):                           
                break
        case 2: 
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("До свидания! Хорошего дня!")
            break
        case _: 
            input_command=input("Для продолжения, введите пункт меню от 1 до 5 => ")
            
