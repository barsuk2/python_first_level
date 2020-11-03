with open('file_for_task2.txt', encoding='utf-8') as f:
    count_str=0
    for line in f:
        # алгоритм построен на предположении, что
        # любое слово заканчивается пробельным сиволом
        print(f'слов в {count_str + 1} строке {line.count(" ") + 1}')
        count_str+=1
    print(f'всего строк {count_str}')
