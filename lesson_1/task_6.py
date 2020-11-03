# dist_day=int(input('сколько км пробежал спортсмен в первый день '))
dist_day = 2
# distance=int(input('сколько км. пробежал спортсмен всего'))
distance = 3
id_days = 1
while True:
    if distance <= dist_day:
        break
    dist_day *= 1.1
    id_days += 1
print(f'на {id_days}-й день спортсмен достиг результата - не менее {distance:.2f} км.')
