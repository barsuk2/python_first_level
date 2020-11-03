class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError



# x = Empty()
# print(x.age1)

class Setattr:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value
        else:
            raise  AttributeError


s = Setattr()
s.age1 = 40
print(s.age)