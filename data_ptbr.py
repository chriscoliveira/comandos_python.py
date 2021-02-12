from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays
# setlocale(LC_ALL,'')
setlocale(LC_ALL, 'pt_BR.utf-8')
dt = datetime.now()
formato = dt.strftime('%A, %d de %B de %Y')
formato1 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formato,' - ',formato1)

# ultimo dia do mes
# from calendar import mdays
mes_atual = int(dt.strftime('%m'))
ano_atual = int(dt.strftime('%Y'))
print(mes_atual,mdays)

total = 0
for m in mdays:
    total += m
print(f'Ultimo dia do mes {mes_atual} é {mdays[mes_atual]}, {ano_atual} tem {total} dias')
