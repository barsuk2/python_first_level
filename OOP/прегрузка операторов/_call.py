class Call:
    """Вызывается при обращении к экземпляру как к функции"""
    def __call__(self, *args, **kwargs):
        print(f'вызваны', args, kwargs)



a = Call()
a(1,2,3,4, a=2 ,s=2)

class C:
    def __init__(self,val):
        self.val = val
    def __call__(self, other):
        return self.val * other

d = C(10)
print(d(2))
print(d(3))