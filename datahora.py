from datetime import datetime, timedelta

#data manual
data = datetime(2020,2,8,18,00,5)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

#cria a data atraves de uma string
data = datetime.strptime('20/04/2019','%d/%m/%Y')
print(data)

#data para timestamp
print(data.timestamp())

#timestamp para data
data = datetime.fromtimestamp(1555729200.0)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

#acrescenta dias a data
data5d = data + timedelta(days=5*10,hours=6 ,minutes=15,seconds=49)
print(data5d.strftime('%d/%m/%Y %H:%M:%S'))

#calcula diferenca de datas
dif = data5d - data
print(dif)
print(dif.seconds)
print(dif.total_seconds())
print(dif.days)