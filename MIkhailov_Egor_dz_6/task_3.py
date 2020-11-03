class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name} '

    def get_total_incom(self):
        return self._income['wage'] + self._income['bonus']


position_1 = Position('arkadiy', 'mikhailov', 'programmer', 15000, 10000)
print(position_1.surname,position_1.surname,position_1.position)
print(position_1.get_full_name())
print(position_1.get_total_incom())
