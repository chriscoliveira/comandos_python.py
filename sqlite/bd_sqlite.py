import sqlite3

# cria a conexao
conexao = sqlite3.connect('database.db')
# cursor
cursor = conexao.cursor()

# cria a tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# # inserir registro
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Joana", 76.6)') # nao use p evitar o sql injection
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)',
#                ('Mel', 10)
#                ) #prefira assim
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'Luiz', 'peso': '55'}
#                ) #ou assim
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Rosa', 'peso': '46'}
#                )
#
# # executa a insercao do registro
# conexao.commit()

# # atualizar dados
# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
#                {'nome': 'Christian', 'id': '2'})

# deleta um registro
# cursor.execute('DELETE FROM clientes WHERE id=:id',
#                {'id': '4'})


conexao.commit()
# exibe os dados da tabela
cursor.execute('SELECT * FROM clientes')

# exibe dados de forma personalizada
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 40})
for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso, sep=' | ')

# finaliza
cursor.close()
conexao.close()
