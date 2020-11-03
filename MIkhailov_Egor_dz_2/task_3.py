# mounth = int(input('введите месяц в виде целого числа'))
# Рещение через dict
mounth = 10
year = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for key, val in year.items():
    if mounth in val:
        print(key)

# решение через list
mounth = 10
year = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
for ind in range(len(year)):
    if mounth in year[ind]:
        print(year[ind][0])
