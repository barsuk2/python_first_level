# slovo= input('строку из нескольких слов')
slovo = 'Строки необходимо пронумеровать. Если в слово длинное'
slovo_list = slovo.split()
for ind, val in enumerate(slovo_list):
    print(ind, val[:10])
