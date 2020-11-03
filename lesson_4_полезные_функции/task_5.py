import functools

my_list = [x for x in range(100, 1000 + 1) if x % 2 == 0]
# print(result_for_recording)
result = functools.reduce(lambda x, y: x * y, my_list)
# print(result)
