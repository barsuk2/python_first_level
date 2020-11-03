import itertools as it
import random


def summa(a):
    res = 0
    for i in a:
        res += dict_kart[i]
    return res


num_cards = [str(i) for i in range(2, 11)]
face_cards = ['J', 'D', 'K', 'A']
mast = [chr(el) for el in range(9828, 9832)]
f =list(it.starmap(lambda x,y: f'{x}{y}', list(it.product(face_cards, mast))))
key = [10] * 12 + [11] * 4
dict_kart = dict(zip(f, key))
d =list(it.starmap(lambda x,y: f'{x}{y}', list(it.product(num_cards, mast))))
q = [[2+x]*4 for x in range(0,9)]
dict_num = dict(zip(d,sum(q,[]) ))
dict_kart.update(dict_num)
koloda = list(dict_kart.keys())
# ИГРА
# 1 ход
# мешаем колоду
stol1 = koloda
random.shuffle(stol1)
print(stol1)
hand1 = [stol1.pop(0) for _ in range(3)]
hand2 = [stol1.pop(0) for _ in range(3)]
print(f'Игороку 1 достались карты {", ".join(hand1)} это очков {summa(hand1)}')
print(stol1)
print(f'Игороку 2 достались карты {", ".join(hand2)} это очков {summa(hand2)}')
