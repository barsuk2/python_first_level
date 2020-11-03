def print_data_user(fname, lname, year_of_birth, city, e_mail, telephone):
    print(
        f'{lname} {fname}, {year_of_birth} года рождения. Город проживания: {city}. '
        f'Контактные данные: E-mail {e_mail}, тел. {telephone}')


print_data_user(fname='Егор', lname='Михайлов', year_of_birth='1976', city='Казань', e_mail='ic@ya.ru',
                telephone='+7904618565')
