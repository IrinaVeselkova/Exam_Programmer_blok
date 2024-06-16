from AnimalRegister import AnimalRegister
from Pets import *
from PackPets import *
from Functions import *

animals_registry=AnimalRegister()
#animals_registry.add('Борька','')

while True:
    match menu():
        case 1: #1.Добавить в реестр
            animals_registry.add(for_one_menu())        
            print("\nЖивотное добавлено в реестр\n")            
        case 2: #2. Показать реестр
            print(f"В регистре находятся:\n{'*'*40}")
            if len(animals_registry) == 0:
                print("В реестре еще нет животных. Добавьте животных в реестр")
            else: print(*animals_registry, sep='\n')
            print('*'*40)
        case 3: #3. Обучить животное
            to_teach_animal_to_commands(animals_registry)            
        case 4: #4. Удалить животное из регистра
            pass
        case 5: #5.Сохранить реестр в файл 
            pass
        case 6: #6. Выход из программы
            print("До свидания! Хорошего дня!")
            break
        case _: #В случае ввода неверного значения
            print ("Для продолжения, введите пункт меню от 1 до 6")
            
