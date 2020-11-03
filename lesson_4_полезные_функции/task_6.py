from itertools import count, cycle
import time


def print_generator_num(num):
    for el in count(num):
        time.sleep(0.5)
        print(el)


# print_generator_num(5)


def print_cycle_list(arg):
    for el in cycle(arg):
        time.sleep(0.5)
        print(el)


l = ['vera', 'nadejda', 'lubov']
# print(print_cycle_list(l))
