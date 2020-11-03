my_list = [30, 25]
while len(my_list) < 10:  # длинна спсика,
    print(my_list)
    num = int(input('ввдите число \n'))
    if num <= min(my_list):
        my_list.append(num)
    for ind in range(len(my_list)):
        if my_list[ind] < num:
            ind_m = my_list.index(my_list[ind])
            my_list.insert(ind_m, num)
            break
