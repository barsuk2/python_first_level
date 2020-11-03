all=[]
ind=0
while True:
    characteristic={}
    article=[]
    add = input('добавить товарную позицию? (нет - запишет измениения)\n')
    if add == 'нет':
        break
    ind+=1
    article.append(ind)
    characteristic['название'] = input('введите название товарной позиции \n')
    characteristic['цена'] = input('введите цену товарной позиции \n')
    characteristic['количество'] = input('введите количество товарной позиции \n')
    characteristic['ед'] = input('введите еденицу измерения товарной позиции \n')
    article.append(characteristic)
    all.append(tuple(article))
print(all)
print('*'*100)
name=[]
price=[]
count=[]
unit=[]
for i in all:
    name.append(i[1]['название'])
    price.append(i[1]['цена'])
    count.append(i[1]['количество'])
    unit.append(i[1]['ед'])

my_dict={'название':name,'цена':price,'количество':count,'eд':unit}
print(my_dict)