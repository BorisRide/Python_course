from data_create import name_data, surname_data, phone_data, address_data
from data_change import print_data_first_sequence, print_data_second_sequence, change_data_first_file, change_data_second_file
from data_delete import delete_data_first_file, delete_data_second_file


def input_data():
# функция ввода и записи данных в файл
    
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n\n"
    f"1 Вариант: \n"                
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"                
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант из предложенных: ")) 

    while var != 1 and var != 2: 
        # проверка правильности ввода даннных пользователем
        print("Неправильный ввод.\n")
        var = int(input('Введите число ещё раз: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
    
    print('Даные записаны в выбранный файл')


def print_data():
# функция вывода данных на консоль (просмотр содержимого файла)
    
    print('Вывожу данные из 1-го файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('Вывожу данные из 2-го файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        data_second_list = []
        k = 0
        for l in range(len(data_second)):
            if data_second[l] == '\n' or l == len(data_second) - 1:
                data_second_list.append(''.join(data_second[k:l+1]))
                k = l
        print(''.join(data_second_list))


def change_data():
# функция корректировки (перезаписи) одной записи в записанных в файлах данных
    
    # выбрать файл (формат записи) для внесения изменений 
    var = int(input(f"В каком файле (варианте формата записи) - первом или втором - Вы хотите изменить данные? \n\n"
    f"1 Вариант: \n"                
    f"Имя \nФамилия \nномер_телефона \nE-mail \n\n"
    f"2 Вариант: \n"                
    f"Имя;Фамилия;номер-телефона;E-mail\n"
    f"Выберите вариант из предложенных: ")) 

    # проверка правильности ввода даннных пользователем
    while var != 1 and var != 2:
        print("Неправильый ввод, такого формата записи нет.\nПовторите ввод.")
        var = int(input('Введите число: '))

    # вывод данных в нумерованном виде    
    if var == 1:
        print_data_first_sequence()
    else:
        print_data_second_sequence()
    
    # найти запись и определить её номер в файле
    num_write = int(input(f"Выберите и укажите номер записи, в которую Вы хотите внести изменения: \n"))
   
    # ввести новый вариант данных, для замены предыдущего
    print('Введите данные для обновления записи: ')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    # замена данных в выбранном файле
    if var == 1:
        change_data_first_file(name, surname, phone, address, num_write)
    else:
        change_data_second_file(name, surname, phone, address, num_write)
    print('Запись изменена.')


def delete_data():
# функция удаления одной записи в записанных в файлах данных
    
    # выбрать файл (формат записи) для внесения изменений 
    var = int(input(f"В каком файле (варианте формата записи) - первом или втором - Вы хотите удалить данные? \n\n"
    f"1 Вариант: \n"                
    f"Имя \nФамилия \nномер_телефона \nE-mail \n\n"
    f"2 Вариант: \n"                
    f"Имя;Фамилия;номер-телефона;E-mail\n"
    f"Выберите вариант из предложенных: ")) 

    # проверка правильности ввода даннных пользователем
    while var != 1 and var != 2:
        print("Неправильый ввод")
        var = int(input('Введите число '))

    # вывод данных в нумерованном виде    
    if var == 1:
        print_data_first_sequence()
    else:
        print_data_second_sequence()
    
    # найти запись и определить её номер в файле
    num_write = int(input(f"Выберите и укажите номер записи, которую Вы хотите удалить: \n"))

    # удаление данных в выбранном файле
    if var == 1:
        delete_data_first_file(num_write)
    else:
        delete_data_second_file(num_write)
    print('Запись удалена')