import random

my_list = [random.randint(0, 10) for _ in range(20)]
print(my_list)
# print({x: result_for_recording.count(x) for x in result_for_recording}) # словарь подсчета количества вхождений - для проверки
print([x for x in my_list if my_list.count(x) == 1])
