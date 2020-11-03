def my_func(a, b):
    # if b > 0 or type(b) is float or a < 0:
    if b > 0 or b%1 != 0  or a < 0:
        return 'число b либо  не  отрицательное, либо не целое. Или число a не положительное '
    # первый способ
    # return 1 /a ** abs(b)
    # втрой способ
    c = a
    for i in range(abs(b) - 1):
        c *= a
    return 1 / c


print(my_func(3, -2.1))
