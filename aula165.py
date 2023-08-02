# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total_do_emprestimo = 1_000_000
data_que_pegou_emprestimo = datetime(2020, 12, 20)
data_para_pagar = relativedelta(years=5)
data_final = data_que_pegou_emprestimo + data_para_pagar

total_datas_das_parcelas = []
data_parcela = data_que_pegou_emprestimo
while data_parcela < data_final:
    total_datas_das_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

total_de_meses_parcelas = len(total_datas_das_parcelas)
valor_das_parcelas = valor_total_do_emprestimo / total_de_meses_parcelas

for data in total_datas_das_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R${valor_das_parcelas:,.2f}')
