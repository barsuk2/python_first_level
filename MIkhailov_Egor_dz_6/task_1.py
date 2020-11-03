from itertools import cycle
import time


class TrafficLight():
    """_"""
    def __init__(self, color='серый'):
        self._color = color
        # self.name = name
        # self.lname = lname

    def running(self, color_timer):
        etalon = ('Красный', 'Желтый', 'Зеленый')
        if etalon != tuple(color_timer.keys()):
            return print('порядок режимов не совпадает с эталоном')
        for color, timer in cycle(color_timer.items()):
            self._color = color
            print(self._color)
            time.sleep(timer)


tl_1 = TrafficLight()
# tl_2 = TrafficLight(name='Гагарина-Воровского', lname='ГВ')


# print(f'Светофорt {tl_1.name} начал свою работу')
tl_1.running({'Красный': 2, 'Желтый': 1, 'Зеленый': 2})  # более "быстрый" светофор для теста
# tl_1.running({'Зеленый': 2, 'Красный': 2, 'Желтый': 1}) # не правильная последовательность
# tl_1.running({'Красный': 7, 'Желтый': 2, 'Зеленый': 5})  # Правильный светофор
print(tl_1._color)