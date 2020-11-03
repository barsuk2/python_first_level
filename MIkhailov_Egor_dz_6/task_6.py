names = []
hours_all = []
with open('file_for_task6.txt', encoding='utf-8') as fl:
    for line in fl:
        # извлекаем название предмета и добавляем в список names'
        names.append(line[:line.index(':')])
        # добавляем в список элементы: цифры и пробелы
        hours = [x for x in line if x.isdigit() or x.isspace()]
        # соединение одиночных цифр преобразованим в строку и опять в список
        line = ''.join(hours).split()
            # print(line)
            # преобразование строковых значений в числа
        line = list(map(int,line))
        hours_all.append(sum(line))
# объединение двух списков в словарь
my_dict = dict(zip(names, hours_all))
print(my_dict)
