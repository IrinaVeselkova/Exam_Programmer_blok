from datetime import date

def for_one_menu():
    while True:
        name=input("Введите имя животного => ").strip()
        if name.isalpha():
            break
        print("Неверный формат имени")
       
    while True:
        match int(input(f"""
    Выберите тип животного:
    1.лошадь
    2.осел
    3.верблюд
    4.кот
    5.собака
    6.хомяк
    {'*'*40}
    введите номер => """)):
            case 1:
                animal_type='лошадь'
                break
            case 2:
                animal_type='осел'
                break
            case 3:
                animal_type='верблюд'
                break
            case 4:
                animal_type='кот'
                break
            case 5:
                animal_type='собака'
                break
            case 6:
                animal_type='хомяк'
                break
            case _:
                print("Выберите из предложенных вариантов")

    while True:
        try:
            day, month, year = input('Введите дату рождения в формате ДД.ММ.ГГГГ =>').split('.')
            birth_date= date(int(year), int(month), int(day))
            break
        except ValueError:
            print('Введенная дата не является корректной, попробуйте еще раз')
    input_command= input("Перечислите команды, которые животные могут выполнять (через запятую),\nили нажмите 'H', чтобы оставить поле пустым => ")
    if input_command.strip().lower() in ("nн"):
          commands = None
    else: commands=[i.strip() for i in input_command.split(',') if i.isalpha()]
    return name, animal_type, birth_date, commands