import sys
from PyQt5.QtWidgets import QApplication
from Piso1 import Mapa

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mapa = Mapa()
    mapa.show()
    sys.exit(app.exec_())
