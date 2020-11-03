class Animal:
    count_in = 0
    @classmethod
    def count(cls):
        cls.count_in +=1
    def __init__(self):
        self.count()

class Bird(Animal):
    count_in = 0

'asdad'.find()


animal_1 = Animal()
animal_2 = Animal()
print(animal_1.count_in)
print(animal_2.count_in)

bird_1 = Bird()
print(bird_1.count_in)
