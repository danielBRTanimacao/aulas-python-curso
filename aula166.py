# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 5))
# print(calendar.monthrange(2023, 1))
# for i, day in list(enumerate(calendar.day_name)):
    # print(i, day)
# numero_primeiro_dia , ultimo_dia = calendar.monthrange(2023, 8)
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2023, 8, ultimo_dia)])
# print(calendar.monthcalendar(2023, 8))
for weeks in calendar.monthcalendar(2023, 8):
    for day in weeks:
        if day == 0:
            continue
        print(day)
