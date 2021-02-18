'''
pip3 install pyqt5

'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        #cria um botao com font 40px e atribui a funcao do click
        self.btn = QPushButton('Texto do botao')
        self.btn.setStyleSheet('font-size:40px;')
        self.btn.clicked.connect(self.acao)

        #adiciona o botao no grid (objeto do botao, linha, coluna, rowspan, colspan)
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        #inicia o grafico
        self.setCentralWidget(self.cw)

    def acao(self):
        print('ola mundo!')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
