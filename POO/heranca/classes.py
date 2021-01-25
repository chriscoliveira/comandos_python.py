class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando..')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando..')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} Estudar..')