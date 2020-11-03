class Car:
    def __init__(self, speed, color, name, is_polece=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polece = is_polece
        # self.turn = turn

    def go(self):
        if self.speed > 0:
            return print(f'Машина {self.name} едет')
        # else: self.stop()

    def stop(self):
        if self.speed == 0:
            return print(f'Машина {self.name} стоит')

    def turn(self, direction=1):
        dict_turn = {1:'вперед',2:'назад',3:'вправо',4:'влево'}
        # self.turn = dict_turn[direction]
        # return print(f'машина {self.name} едет {self.turn}')
        return print(f'машина {self.name} едет {dict_turn[direction]}')


    def show_speed(self):
        return print(f'машина {self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'машина {self.name} превысела разрешенную скорость в 60 км.ч -  {self.speed} км.ч')
        return print(f'машина {self.name} едет со скоростью {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'машина {self.name} превысела разрешенную скорость в  40 км.ч -  {self.speed} км.ч')
        return print(f'машина {self.name} едет со скоростью {self.speed}')

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass



town_car1 = TownCar(54, 'red', 'town_car1')
town_car1.show_speed()
town_car1.speed = 62
town_car1.show_speed()

workcar1 = WorkCar(30, 'yellow','workcar1')
print(workcar1.speed)
workcar1.show_speed()
workcar1.speed = 42

policecar1 = PoliceCar(120, 'blue', 'policecar1', True)
policecar2 = PoliceCar(0, 'blue', 'policecar1', True)
policecar1.show_speed()

policecar2.stop()
policecar1.turn()
policecar1.turn(2)
