import random

my_list = [random.randint(0, 100) for _ in range(20)]
print(my_list)
result = [my_list[ind] for ind in range(1, len(my_list)) if my_list[ind - 1] < my_list[ind]]
print(result)
