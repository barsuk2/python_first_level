# with open("file_for_task3.txt", encoding='utf-8') as f:
#     result_for_recording = [x.rstrip().split() for x in f]
# summa = 0
# for i in range(len(result_for_recording)):
#     summa += int(result_for_recording[i][-1])
#     if int(result_for_recording[i][-1]) < 20000:
#         print(f'сотрудник {result_for_recording[i][0]} имеет з/п менше 20000')
# print(f'Средняя з.п {summa / len(result_for_recording)}')
# print('*'*20)
sum_profit = 0
with open("file_for_task3.txt", encoding='utf-8') as f:
    for ind,line in enumerate(f,1):
        name = line[:line.index(' ')]
        profit = int(line[line.index(' '):].lstrip())
        if profit < 20000:
            print(f'сотрудник {name} имеет з/п менше 20000')
        sum_profit += profit
print(f'Средняя з.п {sum_profit / ind}')
