class WindowDoor:
    def __init__(self, width, height):
        # self.width = width
        # self.height = height
        self.area = width * height


class Room:
    unit = 'm'

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.volume_room = self.length * self.width * self.height
        self.area_walls = 2 * self.height * (self.length + self.width)
        self.winow_door = 0

    def add_wd(self, wd_width, wd_height):
        self.winow_door += (WindowDoor(wd_width, wd_height).area)

    def print_volume_room(self):
        print(f'The volume of the room - {self.volume_room} {Room.unit}3')

    def print_area_walls(self):
        print(f'The area of the walls {self.area_walls} {Room.unit}2')

    def area_walls_sub_wd(self):
        print (f'Area windows and doors   = {self.winow_door}')
        print (f'Area room  = {self.area_walls - self.winow_door}')


romm_1 = Room(5, 2, 2.5)
romm_1.print_area_walls()
romm_1.print_volume_room()
romm_1.add_wd(2,2)
romm_1.add_wd(1,1)
romm_1.add_wd(2.6,0.8)
romm_1.area_walls_sub_wd()

class WindowDoor_1:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height

class Room1:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []
    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor_1(wd_len, wd_height).square)
    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square

r = Room1(7, 4, 3.7)
print(r.square)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
print(r.wd)