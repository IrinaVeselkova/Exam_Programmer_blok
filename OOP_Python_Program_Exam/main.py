from AnimalRegister import AnimalRegister
from Pets import *
from PackPets import *
from Functions import *

animals_registry=AnimalRegister()
while True:
    match menu():
        case 1: #1.Добавить в реестр
            animals_registry.add(for_one_menu())
            print("Животное добавлено в реестр")
            if input("Перейти в меню? (Д/Н)").strip().lower() not in ('д', "y"):                           
                break
        case 2: #2. Показать реестр
            print(f"В регистре находятся:\n{'*'*40}")
            if len(animals_registry) == 0:
                print("В реестре еще нет животных. Добавьте животных в реестр")
            else: print(*animals_registry, sep='\n')
            print(f"В регистре находятся:\n{'*'*40}")
            if input("Перейти в меню? (Д/Н)").strip().lower() not in ('д', "y"):                           
                break
        case 3: #3. Обучить животное
            pass
        case 4:
            pass
        case 5:
            pass
        case 6: 
            print("До свидания! Хорошего дня!")
            break
        case _: 
            input_command=input("Для продолжения, введите пункт меню от 1 до 5 => ")
            
