print(f"Вы работаете с реестром домашних животных.\nВыберите пункт меню:\n{'*'*40}", end='')
print('''
1.Добавить в реестр новое животное\n
2.Показать реестр\n
3.Обучить животное новой команде\n
4.Удалить животное из реестра\n
5.Выйти из реестра'''+'\n'+'*'*40+'\n')
input_command=input("Пункт меню => ")
flag=True
while flag:
    match int(input_command):
        case 1:
            pass
        case 2: 
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            flag = False
            print("До свидания! Хорошего дня!")
        case _: 
            input_command=input("Для продолжения, введите пункт меню от 1 до 5 => ")
            