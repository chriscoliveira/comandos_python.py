from classes import Cliente

cliente1 = Cliente('Christian', 36)
cliente1.insere_endereco('Caraguatatuba', 'SP')
cliente1.insere_endereco('Jacarei', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Patricia', 40)
cliente2.insere_endereco('Sao Paulo', 'SP')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Luiz', 55)
cliente3.insere_endereco('Sao Bernardo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('#'*50)