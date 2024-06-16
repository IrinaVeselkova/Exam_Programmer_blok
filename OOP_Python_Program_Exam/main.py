from AnimalRegister import AnimalRegister
from Pets import *
from PackPets import *
from Functions import *


while True:
    match menu():
        case 1: #1.Добавить в реестр
            AnimalRegister.animals_registry.add(for_one_menu())
            print("Животное добавлено в реестр")
            if input("Перейти в меню? (Д/Н)").strip().lower() not in ('д', "y"):                           
                break
        case 2: #2. Показать реестр
            print(f"В регистре находятся:\n{'*'*40}")
            if len(AnimalRegister.animals_registry) == 0:
                print("В реестре еще нет животных. Добавьте животных в реестр")
            else: print(*AnimalRegister.animals_registry, sep='\n')
            print(f"В регистре находятся:\n{'*'*40}")
            if input("Перейти в меню? (Д/Н)").strip().lower() not in ('д', "y"):                           
                break
        case 3: #3. Обучить животное
            
            to_teach_animal_to_commands()
        case 4: #4. Удалить животное из регистра
            pass
        case 5: #5.Сохранить реестр в файл 
            pass
        case 6: #6. Выход из программы
            print("До свидания! Хорошего дня!")
            break
        case _: #В случае ввода неверного значения
            input_command=input("Для продолжения, введите пункт меню от 1 до 6 => ")
            
