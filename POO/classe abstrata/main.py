from cp import ContaPoupanca
from cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

print('#'*50)

cc = ContaCorrente(agencia=1111,conta=3333,saldo=0,limite=500)
cc.depositar(100)
cc.sacar(300)
cc.sacar(350)
cc.depositar(1000)


