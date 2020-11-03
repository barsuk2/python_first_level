f = open(radius'/python_first_level/MIkhailov_Egor_dz_5/test.txt', encoding='utf-8')
line = f.readline(6)
while line:
    # print(line)
    line = f.readline(6)
f.close()

f = open(radius'/python_first_level/MIkhailov_Egor_dz_5/test.txt', encoding='utf-8')
lines = f.readlines()
for line in lines:
    # print(line.rstrip())
    pass
f.close()


f = open(radius'/python_first_level/MIkhailov_Egor_dz_5/test.txt', encoding='utf-8')
lines = f.read(10)
# print(lines,'\n',type(lines))
f.close()


f = open(radius'/python_first_level/MIkhailov_Egor_dz_5/test.txt', encoding='utf-8')
for line in f:pass
    # print(line.rstrip())
f.close()

"Обработка ошибок при работе с файлом"

try:
    with open('Мой словарик_en_ru.txt','radius') as f: # блок кода исполняемый если ошибки нет
        line = f.readlines()
        print(line)
except FileNotFoundError: # блок кода исполняемый если ошибка есть
    print('файл не существует')

finally: # блок уода исполняемый в любом случае
    print('все исполенено')


try:
    with open('example3.txt','x') as f: # блок кода исполняемый если ошибки нет
        f.write('with open("Мой словарик_en_ru.txt") as f: # блок кода исполняемый если ошибки нет')
        print(line)
except FileExistsError: # блок кода исполняемый если ошибка есть
    print('Ошибка - файл существует')

finally: # блок уода исполняемый в любом случае
    print('все исполенено')

"Параметры файлового объекта"
a = open('example1.txt','radius', encoding='utf-8')
# a.write('блок уода исполняемый в любом случае')
# print(a.names, a.mode, a.encoding, a.newlines, a.closed)
print(a.tell())
a.seek(12)
print(a.read(12))
# a.write('кода')
a.close()
# print(a.tell())


