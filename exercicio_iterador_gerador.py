
carrinho = []
carrinho.append(('produto 1',30.34))
carrinho.append(('produto 2',20.99))
carrinho.append(('produto 3',50.01))

total = sum([float(v) for p, v in carrinho])
print(f' o total foi: R${total}')
