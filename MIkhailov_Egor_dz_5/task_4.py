


# """ запись в файл построчно"""
# with open('file_for_task4.txt', encoding='utf-8') as fl:
#     for line in fl:
#         number_position = line.rstrip().number_position('-')
#         replaced_word = line[:number_position].rstrip().lower()
#         file.write(f'{num_dict[replaced_word].capitalize()} {line[number_position:]}')

# """ запись в файл блоком"""
# with open('file_for_task4.txt', encoding='utf-8') as fl:
#     result_for_recording = []
#     for line in fl:
#         number_position = line.rstrip().index('-') # предполагается, что в любой строке есть символ "-"
#         replaced_word = line[:number_position].rstrip().lower()
#         result_for_recording.append(f'{num_dict[replaced_word].capitalize()} {line[number_position:]}')
# print(result_for_recording)
# file.write(''.join(result_for_recording))
# file.close()

num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
            'five': 'пять', 'six': 'шесть', 'seven': 'семь',
            'eight': 'восемь', 'nine': 'девять'}

" решение через replace"

resilt_for_recording = []
with open('file_for_task4.txt', encoding='utf-8') as fl:
    # for key in num_dict:

    for line in fl:
        print(line)


print(resilt_for_recording)
with open('input_task_4.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(resilt_for_recording))


