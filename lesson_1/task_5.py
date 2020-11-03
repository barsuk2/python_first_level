profit=int(input('Введите выручку вашей фирмы '))
expenses=int(input('Введите издерхки вашей фирмы '))
if profit-expenses >0:
    print (f'Финансовый результат - Прибыль {profit - expenses}')
    print (f'Рентабелльность - {(profit - expenses) / profit}')
    workers=int(input('Сколько сотрудников работеает в ващей фирме \n'))
    print (f'Прибыль фирмы расчете на одного сотрудника {(profit - expenses) / workers}')

else:
    print ('Финансовый результат - Убыток')
