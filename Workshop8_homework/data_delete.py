def delete_data_first_file(num_of_write):
# функция удаления данных в файле data_first_variant
    
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list_left = [] # часть файла слева от удаляемой записи
        data_first_list_right = [] # часть файла справа от удаляемой записи
        start = num_of_write*5 - 5
        stop = num_of_write*5
        for i in range(start):
            data_first_list_left.append(data_first[i])
        for j in range(stop, len(data_first)):
            data_first_list_right.append(data_first[j])
                   
        data_first = data_first_list_left + data_first_list_right
        
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for o in range(len(data_first)):
                f.write(f'{data_first[o]}')


def delete_data_second_file(num_of_write):
# функция удаления данных в файле data_second_variant
    
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        data_second_list_left = [] # часть файла слева от удаляемой записи
        data_second_list_right = [] # часть файла справа от удаляемой записи
        start = num_of_write*2 - 2
        stop = num_of_write*2
        for i in range(start):
            data_second_list_left.append(data_second[i])
        for j in range(stop, len(data_second)):
            data_second_list_right.append(data_second[j])
                    
        data_second = data_second_list_left + data_second_list_right

        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for o in range(len(data_second)):
                f.write(f'{data_second[o]}')