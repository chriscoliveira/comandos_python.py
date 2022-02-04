from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_veiculo(self) -> None: pass

class CarroLuxo(Veiculo):
    def buscar_veiculo(self) -> None:
        print('Carro de luxo esta buscando o cliente...')

class CarroPopular(Veiculo):
    def buscar_veiculo(self) -> None:
        print('Carro popular esta buscando o cliente...')

class MotoLuxo(Veiculo):
    def buscar_veiculo(self) -> None:
        print('Moto de luxo esta buscando o cliente...')

class MotoPopular(Veiculo):
    def buscar_veiculo(self) -> None:
        print('Moto popular esta buscando o cliente...')

class VeiculoFactory(ABC):
    def __init__(self,tipo) :
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self) -> None:
        self.carro.buscar_veiculo()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        elif tipo == 'popular':
            return CarroPopular()
        elif tipo == 'moto_luxo':
            return MotoLuxo()
        elif tipo == 'moto_popular':
            return MotoPopular()
        else:
            raise ValueError('Tipo de veiculo nao existe')

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        else:
            raise ValueError('Tipo de veiculo nao existe')

if __name__ == '__main__':
    from random import choice
    veiculos_zona_norte = ['luxo', 'popular', 'moto_luxo', 'moto_popular']
    veiculos_zona_sul = ['popular']

    print('Zona Norte')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_zona_norte))
        carro.buscar_veiculo()

    print('\nZona Sul')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_zona_sul))
        carro2.buscar_veiculo()