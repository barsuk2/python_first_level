def func_division(num_1, num_2):
    itog =  num_1 / num_2 if num_2 != 0 else 'False'
    return itog


print(f'{func_division(1, 0):.4}')
