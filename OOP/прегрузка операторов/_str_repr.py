class A:
    def __init__(self,value=0):
        self.data = value
    def __add__(self, other):
        self.data += other
    def __repr__(self):
        return f'метод repr {self.data}'
    def __str__(self):
        return f'метод __str__ {self.data}'
x= A(2)
x+1
print(x)
str(x)
print(x,repr(x)+'asd')
