"""Условие задачи требует дополнительных разъяснений. Скорее всего имелось ввиду это"""
import itertools
import time

start = time.perf_counter()


def fact_gen():
    fact = 1
    for el in itertools.count(1):
        if el > 15: break
        fact = fact * el
        yield el, fact


for i in fact_gen():
    print(f'факториал числа {i[0]} это {i[1]}')

print('\n', '*' * 50)
print(f'время работы скрипта - {time.perf_counter() - start:.10f} сек.')

Здравствуйте. Хочу задать вопрос по git.
Вопрос по SSH. Я сдел так как описано в уроке.
1. Cгенерировал ssh-keygen, и т д.

А как правильно настроить ssh на другом компьтере для клонирования моего репозитория