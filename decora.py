def master(funcao):
    def slave(*args,**kwargs):
        print('agora estou decorada')
        funcao(*args,**kwargs)
    return slave

@master
def fala_oi():
    print('Oi\n')

@master
def outrafuncao(msg):
    print(msg)

fala_oi()

outrafuncao('Olah')

from time import time, sleep

def velocidade(funcao1):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao1(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time)*1000
        print(f' a funcao "{funcao1.__name__}" levou {tempo:.8f}ms para executar')
    return interna

@velocidade
def demora():
    for i in range(10000):
        print(i, end='')

demora()