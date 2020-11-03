# user_time=int(input('Введите время в секундах '))
user_time=120
user_hour=user_time//3600
user_min=user_time%3600//60
user_sek=user_time%60
if len(str(user_hour))==1:
    user_hour='0'+str(user_hour)
if len(str(user_min))==1:
    user_min='0'+str(user_min)
if len(str(user_sek))==1:
    user_sek='0'+str(user_sek)
print(f'{user_hour}:{user_min}:{user_sek}')

