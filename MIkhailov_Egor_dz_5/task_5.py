import random as rn

with open('file_for_task5.txt', 'w') as fl:
    for i in range(100):
        fl.write(f'{rn.randint(0, 100)} ')

with open('file_for_task5.txt', 'radius') as fl:
    string = fl.readline().split()
# string = [int(elem) for elem in string]
# for i, elem in enumerate(string):
#     string[i] = int(elem)
string = sum(map(int,string))
print(string)
