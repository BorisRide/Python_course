from logger import input_data, print_data, change_data, delete_data

def interface():
    print("Добрый день! Вы попали на бот-справочник от студента-тестировщика GeekBrains ;) \n 1 - запись данных \n 2 - вывод данных \n 3 - перезапись данных \n 4 - удаление данных")
    command = int(input('Введите число: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        # проверка правильности ввода данных пользователем
        print("Неправильный ввод, такой команды нет.\nПовторите ввод: ")
        command = int(input('Введите число: '))

    if command == 1:
        input_data() # вызов функции ввода данных записной книжки и записи даннывх в файл
    elif command == 2:
        print_data() # вызов функции печати данных записной книжки
    elif command == 3:
        change_data() # вызов функции перезаписи данных записной книжки
    elif command == 4:
        delete_data() # вызов функции удаления данных записной книжки