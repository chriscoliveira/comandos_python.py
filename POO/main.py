from pessoa import Pessoa

p1 = Pessoa('Christian',37)
p2 = Pessoa('Patricia',40)

p1.falar('POO')
p2.falar('Facebook')
p1.comer('Sorvete')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


print(p1.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())
print(p1.gera_id())