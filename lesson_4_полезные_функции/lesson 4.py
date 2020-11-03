# import random
# "(1:8]"
# # (x for x)
# result_for_recording = (random.random() for i in range(20000000))
# # my_list1 = [x for x in range(5)]
# p=[x for x in result_for_recording if x == 0]
# print(len(p))
#
# глубина 27 см
# высота от 16 до 20
# list
# set - множество
# tuple - кортеж
#
#     # result_for_recording = [random.randint(0, 10) for _ in range(20)]
#     # print(result_for_recording)
#     # print({x: result_for_recording.count(x) for x in result_for_recording}) # словарь подсчета количества вхождений - для проверки
#     # print([x for x in result_for_recording if result_for_recording.count(x) == 1])

a = [1, 2, 3]
g = [4, 5, 6]
g1 = [4, 5, 6]
g2 = [4, 5, 6]
b = "xyz"
li = ([1, 2, 3], 'xyz')
print(sum(li,[]))
# преобразовывает набор последовательностей в одну

print(sum([list(i) for i in zip(a, b, g)], []))

my_dict1 = dict(zip(b,a))
my_dict2 = dict(zip(b,g))

def preobraz_neskol_spiskov_v_odin(*args):
    """Пребразование нескольких списков в один. Списки должны быть одинаковой длинны"""
    return sum(list(args), [])


def preobraz_neskol_slovar_v_odin(**kwargs):
    """Пребразование нескольких списков в один. Списки должны быть одинаковой длинны"""
    return kwargs

# print(list(map(lambda x: x.upper(),'old_list')))
# print(list(int,'old_list')))
" пример использования map"

"filter"
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'не просто', 'просо', 'мак']
print(list(filter(lambda x: x != 'мак',mixed)))


# print(preobraz_neskol_spiskov_v_odin(a, g, g1, g2))
print(preobraz_neskol_slovar_v_odin(q=10,q2=12))


import time
for i in range(10**10):
    print(i)
    time.sleep(10)