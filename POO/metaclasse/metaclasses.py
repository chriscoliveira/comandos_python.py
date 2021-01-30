class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name =='A':
            return type.__new__(mcs,name,bases,namespace)
        print(namespace)
        if 'b_fala' not in namespace:
            print(f'vc precisa criar o metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'o metodo b_fala, precisa ser um metodo e nao atributo em {name}')
class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    def seila(self):
        pass

    def b_fala(self):
        pass