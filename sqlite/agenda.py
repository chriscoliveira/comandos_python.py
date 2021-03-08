import sqlite3


class AgendaBD:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome,telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()
        agenda.listar()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?,telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()
        agenda.listar()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()
        agenda.listar()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    agenda = AgendaBD('agenda.db')
    # agenda.inserir('Christian', '111111')
    # agenda.editar('Rosa', '000000', 13)
    # agenda.listar()
    # agenda.excluir(14)
    agenda.buscar('patricia')
    agenda.listar()
