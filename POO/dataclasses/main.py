from dataclasses import dataclass


@dataclass(eq=True, repr=True, order=False, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(f'Tipo invalido {type(self.nome).__name__} != str em {self}')

    @property
    def nomeCompleto(self):
        return f'Nome Completo: {self.nome} {self.sobrenome}'


p1 = Pessoa('Christian', 'Carvalho')
# p2 = Pessoa(2, 'Carvalho')
# print(p1 == p2)

# print(p1.nome, "-", p1.sobrenome)
print(p1)
print(p1.nomeCompleto)
