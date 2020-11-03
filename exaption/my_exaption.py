def fetcher(arg, ind):  # извлекать
    return arg[ind]


def catcher():
    try:
        fetcher('qweqe', 2)
    except IndexError:
        print("Ошибка индекса")
    print('продолжаем')

try:
    raise ValueError # Возбуждение исключение вручную
except ValueError:
    print("Исключение возбуждено")

# assert False, "Nobody expects the Spanish Inquisition!"

try:
    fetcher('qwe',4)
finally:
    print("Выпролнить в любом случае")
    print(10**2)

