""""""
import json

result_for_recording = []
total_profit = []
with open('file_for_task7.txt', encoding='utf-8') as file:
    for line in file:
        tmp_dict = {}
        # очистка от символа '.'
        my_list = line.replace('.', '').split()

        profit = int(my_list[-2]) - int(my_list[-1])

        if profit > 0:
            total_profit.append(profit)
        tmp_dict[my_list[0]] = profit
        result_for_recording.append(tmp_dict)
average_profit = {'average_profit': round(sum(total_profit) / len(total_profit), 2)}
result_for_recording.append(average_profit)

with open('user_7_task.json', 'w', encoding='utf-8') as f:
    json.dump(result_for_recording, f)

with open('user_7_task.json', 'radius', ) as f:
    print(json.load(f))
