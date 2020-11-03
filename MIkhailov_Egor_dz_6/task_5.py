class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск рисования')


class Pencil(Stationery):
    def draw(self):
        print('Запуск письма')


class Handle(Stationery):
    def draw(self):
        print('Запук закрашивания')

pen = Stationery('printer')
pen1 = Pen('Pen')
pen2 = Pencil('Pencil')
pen3 = Handle('Handle')

pen.draw()
pen1.draw()
pen2.draw()
pen3.draw()

