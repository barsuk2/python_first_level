import datetime
now = datetime.datetime.now()
date_str = f'{now.day:02}-{now.month:02}-{now.year}'
print(date_str)


class Data:
    date_ = '23-05-2020'
    @staticmethod
    def parse():
        Data.date_ = Data.date_.split('-')
        # return print(Data.date_)
        Data.date_ = tuple(map(int, Data.date_))
        # Data.date_ = (23, 16, 2020)
        return Data.date_

    @classmethod
    def validator(cls):
        if cls.date_[1]  in range(1,13):
            return 'Validation true'
        else:
            return 'Validation not true'



mydate = Data()
print(Data.parse())
print(Data.validator())



