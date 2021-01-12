# def func(a1, a2, a3, a4, a5):
#     print(a1, a2, a3, a4, a5)
#
#
# func(1, 2, 3, 4, 5)


# def funcargs(*args):
#     print(args)
#     print(args[-1])
#     print(len(args))
#
# funcargs(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


# def funcargs(*args):
#     for v in args:
#         print(v)
#
# funcargs(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


# def funcargs(*args):
#     print(args)
#     print(args[0])
#     print(len(args))
#
# lista= [1,2,3,4,5,6,7,8,9]
# funcargs(*lista,'christian','patricia')


def funckwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'])
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
funckwargs(lista, nome='Christian', sobrenome='Carvalho', idade='36')
