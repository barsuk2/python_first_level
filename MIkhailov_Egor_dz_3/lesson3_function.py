import math

PI = 3.14  # Константы питшуться UPEER
PI = math.pi


def calc_circle_area(radius):
    return PI * radius ** 2


r = 12
print(f'Площадь круга радиусом {r} равна {calc_circle_area(r):.2f}')


def calc_area_box(width, height=None):
    return width * height if height is not None else width


a = "Площадь круга радиусом {r} равна".split()
str_d = {}
first, *a1, last = a
str_d['first'] = first
str_d['last'] = last
str_d['center'] = a1
print(str_d)


def disp_str_d(*args):
    a, b, c, *d = args
    a1 = (a, b, ' '.join(c), f'доп параметр {" ".join(d)}')
    return a1


# str_d['qwe'] = 'qwe2'
print(disp_str_d(*str_d.values()))
str_d['center'] = 'круга'
print(str_d)
str_d = {'first': 'Площадь', 'last': 'равна', 'center': 'круга'}


def upper_dict(**kwargs):
    """

    :param kwargs:
    :return:
    """
    last, *first = kwargs.values()

    return last.upper(), ' '.join(first).upper()


# print(upper_dict(**str_d).__doc__)

"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и 
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
обработку ситуации деления на ноль."""


def difinition(*args):
    if len(args) != 2:
        return 'Введите  два числа'
    a, b = args
    if b == 0:
        return 'Второе число не должно быть нулем'
    return a / b


# print((difinition(5,0,)))

'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, 
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.'''
import random


def display_user(**kwargs):
    name, lname, bd, city, e_mail, phone, *other = kwargs.values()
    result = f' имя пользователя {name} фамилия {lname} год {bd} город {city}\n почта{e_mail} телефон{phone}'
    if other == []:
        print(result)
    else:
        print(f'{result} прочие {" ".join(other)}')


a = ['name', 'lname', 'bd', 'city', 'e_mail', 'fon', ]
my_dict = {}
for ind, val in enumerate(a):
    my_dict[val] = f'{random.choice(a)} user{random.randint(0, 10)}'

print(my_dict)
my_dict['qwe'] = 'qwe'
display_user(**my_dict)

d = []
print(d == [])

"""3. Реализовать функцию my_func(), 
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""


def my_funk(*args):
    l = list(set(args))
    l.remove(min(l))
    print(sum(l))

def my_funk2(*args):
    l = list(set(args))
    min_ = l[0]
    for i in l:
        if min_ >= i:
            min_= i
    idx = l.index(min_)
    del l[idx]
    print(sum(l))

my_funk2(4,3,10)
print('*'*20)
l =[12,23,33]
def qwe(x):
    return x**2


s =[x**2 for x in l]
print(s)
print(set(zip([1,2],[3,4])))

print([x for x in map((lambda x: x*2 if x%2 !=0 else x),l)])
print([x*2 for x in l if x%2 !=0 ])
