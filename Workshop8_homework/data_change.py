def print_data_first_sequence():
# функция вывода нумерованных данных из первого файла
    
    print('Вывожу нумерованные данные из 1-го файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list_sequence = []
        m = 1
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                if m == 1:
                    data_first_list_sequence.append(f'{str(m)}\n')
                else:
                    data_first_list_sequence.append(f'{str(m)}')
                data_first_list_sequence.append(''.join(data_first[j:i+1]))
                m +=1
                j = i
        print(''.join(data_first_list_sequence))

def print_data_second_sequence():
# функция вывода нумерованных данных из второго файла
    
    print('Вывожу нумерованные данные из 2-го файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        data_second_list_sequence = []
        n = 1
        k = 0
        for l in range(len(data_second)):
            if data_second[l] == '\n' or l == len(data_second) - 1:
                if n == 1:
                    data_second_list_sequence.append(f'{str(n)}\n')
                else:
                    data_second_list_sequence.append(f'{str(n)}')
                data_second_list_sequence.append(''.join(data_second[k:l+1]))
                n +=1
                k = l
        print(''.join(data_second_list_sequence))


def change_data_first_file(ch_name, ch_surname, ch_phone, ch_address, num_of_write): 
# функция изменения данных в файле data_first_variant
    
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list_left = [] # часть файла слева от изменяемой записи
        data_first_list_right = [] # часть файла справа от изменяемой записи
        data_first_list_middle = [] # список с новой записью
        start = num_of_write*5 - 5
        stop = num_of_write*5
        for i in range(start):
            data_first_list_left.append(data_first[i])
        for j in range(stop, len(data_first)):
            data_first_list_right.append(data_first[j])
        for k in range(1, 6):
            if k == 1:
                data_first_list_middle.append(f'{ch_name}\n')
            elif k == 2:
                data_first_list_middle.append(f'{ch_surname}\n')
            elif k == 3:
                data_first_list_middle.append(f'{ch_phone}\n')
            elif k == 4:
                data_first_list_middle.append(f'{ch_address}\n\n')
            
        data_first = data_first_list_left + data_first_list_middle + data_first_list_right
        """# проверка правильности изменения данных:
        data_first_list = []
        m = 0
        for n in range(len(data_first)):
            if data_first[n] == '\n' or n == len(data_first) - 1:
                data_first_list.append(''.join(data_first[m:n+1]))
                m = n
        print('проверка замены данных: \n')
        print(''.join(data_first_list))"""

        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for o in range(len(data_first)):
                f.write(f'{data_first[o]}')

        
def change_data_second_file(ch_name, ch_surname, ch_phone, ch_address, num_of_write): 
# функция изменения данных в файлах data_second_variant
    
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        data_second_list_left = [] # часть файла слева от изменяемой записи
        data_second_list_right = [] # часть файла справа от изменяемой записи
        data_second_list_middle = [] # список с новой записью
        start = num_of_write*2 - 2
        stop = num_of_write*2
        for i in range(start):
            data_second_list_left.append(data_second[i])
        for j in range(stop, len(data_second)):
            data_second_list_right.append(data_second[j])
        for k in range(1, 6):
            if k == 1:
                data_second_list_middle.append(f'{ch_name};')
            elif k == 2:
                data_second_list_middle.append(f'{ch_surname};')
            elif k == 3:
                data_second_list_middle.append(f'{ch_phone};')
            elif k == 4:
                data_second_list_middle.append(f'{ch_address}\n\n')
            
        data_second = data_second_list_left + data_second_list_middle + data_second_list_right

        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for o in range(len(data_second)):
                f.write(f'{data_second[o]}')