class A:
    """Метод add обрабатывает счложение справа
    мето radd обрабатывает + слева"""
    def __init__(self, val=1):
        self.val = val
    def __add__(self, other):
        return self.val + other
    def __radd__(self, other):
        return other+self.val

class Iadd:
    """поддержку комбинированной операции сложения +="""
    def __init__(self, val=1):
        self.val = val
    # def __add__(self, other):
    #     return self.val + other
    def __iadd__(self, other):
        self.val += other
        return self
s =A(10)
sa = A(20)
print(10+s)

x = Iadd()
x+=1
x+=1
print(x.val)