class Minhalista:
    def __init__(self):
        self.__items = []
        self.__index = 0
    def add(self,valor):
        self.__items.append(valor)

    def __getitem__(self, item):
        return self.__items[item]

    def __setitem__(self, key, value):
        if key >= len(self.__items):
            self.__items.append(value)
        self.__items[key] = value

    def __delitem__(self, key):
        del self.__items[key]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'


if __name__ == '__main__':
    lista = Minhalista()
    lista.add('Luiz')
    lista.add('Maria')
    print(lista)
    lista[1] = 'Christian'
    print(lista)
    lista[2] = 'Patricia'
    print(lista)
    del lista[0]
    print(lista)
    #
    # for valor in lista:
    #     print(valor)
