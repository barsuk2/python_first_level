my_list = []
while True:
    list_elem = input('введите следующий элемент последовательности (для запуска модификации данных введите  run)\n')
    if list_elem != 'run':
        my_list.append(list_elem)
        print(my_list, id(my_list))
    else:
        if len(my_list) % 2 == 0:
            my_len = len(my_list)
        else:
            my_len = len(my_list) - 1
        for i in range(0, my_len, 2):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        print(my_list, id(my_list))
        break
