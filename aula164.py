# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

format_ = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2023-07-26 13:34:07', '%Y-%m-%d %H:%M:%S')
print(data.strftime(format_))
print(data.strftime('%Y'), data.year)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)
