# number=input('введите целое, положительное число ')
number = str(188882228233)
list_number = list(number)
max_elem = list_number[0]

while len(list_number) > 0:
    if int(max_elem) - int(list_number[-1]) <= 0: max_elem = list_number[-1]
    # del list_number[-1]
    list_number.pop()

print(f'максимальная цифра в числе {number} это {int(max_elem)}')
