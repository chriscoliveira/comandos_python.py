#
# def divide(n1,n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as error:
#         print(f'Erro: {error}')
#         raise
#
# try:
#     print(divide(2,0))
# except ZeroDivisionError as error:
#     print(error)

def divide(n1,n2):
    if n2 == 0:
        raise ValueError('N2 nao pode ser zero')
    return n1/n2

try:
    print(divide(2,0))
except ValueError as erro:
    print(erro)