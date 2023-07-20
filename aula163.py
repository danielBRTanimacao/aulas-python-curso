# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

format_ = '%d/%m/%Y %H:%M:%S'
data_start = datetime.strptime('13/05/2004 00:00:00', format_)
data_end = datetime.strptime('15/08/2013 12:45:03', format_)

# delta = timedelta(days=10)
delta = relativedelta(data_start, data_end)
print(delta.days)

# print(data_end + delta)
# print(data_end + relativedelta(seconds=50))

# print(delta.total_seconds())
# delta = data_end - data_start
# print(delta.days, delta.seconds)
# print(data_start > data_end)
# print(data_start < data_end)
# print(data_start == data_end)