# решение через global


# sum_all_values = 0
#
#
# def sum_num(args):
#     global sum_all_values
#     args = args.split()
#     for number_position in range(len(args)):
#         args[number_position] = int(args[number_position])
#     sum_all_values += sum(args)
#     return sum_all_values
#
#
# while True:
#     numbers = input('введите числа , разделенные пробелом (для выхода из программы введите "q") \n')
#     if 'q' in numbers:
#         numbers = numbers.replace('q', '')
#         print(sum_num(numbers))
#         break
#     print(sum_num(numbers))


sum_all_values = 0


def sum_numbers(args, sum_all_values):
    args = args.split()
    for i in range(len(args)):
        args[i] = int(args[i])
    sum_all_values += sum(args)
    return sum_all_values


while True:
    numbers = input('введите числа, разделенные пробелом (для выхода введите "q") \n')
    if 'q' in numbers:
        # numbers = numbers[:-2]
        numbers = numbers.replace('q', '')
        sum_all_values = sum_numbers(numbers, sum_all_values)
        print(sum_all_values)
        break
    sum_all_values = sum_numbers(numbers, sum_all_values)
    print(sum_all_values)
