import time


class Blog:
    def __init__(self):
        self.sum_blogs = []
        # self.ind = in

    def add(self, blog):
        return self.sum_blogs.append(blog)

    def __iter__(self):
        return BlogIter(self.sum_blogs)


class BlogIter:
    def __init__(self, series):
        self.series = series
        self.ind = 0

    def __next__(self):
        if self.ind <= len(self.series):
            self.ind += 2
            return self.series[self.ind]
        raise StopIteration


#
# sports_blog = Blog()
# sports_blog.add(
#                 ' совещание по рынку труда, по итогам встречи президент\n')
#
# sports_blog.add(
#                 'С 1 июня москвичи смогут посещать все парки и зеленые зоны, кроме парка «Зарядье». '
#                 'Об этом сообщил мэр Сергей Собянин.\n'
#                 )
#
# sports_blog.add(
#                 'Как заявила пресс-служба Шестого флота ВМС США, накануне два российских истребителя Су-35 '
#                 '"небезопасно" перехватили американский самолет-разведчик Poseidon P-8A над Средиземным морем.\n'
#                 )
#
#
# for el in sports_blog:
#     print(el)

class Squaers:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        self.start += 1
        return self.start ** 2

# l = Squaers(5,10)
# print([x for x in l])
#
# print([x for x in l])
#
# print(list(Squaers(1,3)))

# l1 = iter(l)
# print(next(l1))


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offcet = 0
    def __next__(self):
        if self.offcet>=len(self.wrapped):
            raise StopIteration
        else:
            item= self.wrapped[self.offcet]
            self.offcet +=2
            return item

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

sk = SkipObject('abcdfghiklmnopqrstuwyz')
i= iter(sk)
print(next(i),next(i),next(i))
for i in sk:
    print(i)