"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste

        print('eu sou o NEW')
        return super().__new__(cls)

    def __init__(self):
        print('eu sou o INIT')

    def __call__(self, *args, **kwargs):
        resultado = 1
        for i in args:
            resultado *= i
        return resultado

    def __setattr__(self, key, value):
        self.__dict__[key] = value

a = A()
variavel = a(1, 2, 3, 4, 5, nome='Christian')
b = A()
c = A()

print(variavel)


a.nome = 'Christian'
print(a.nome)