import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect

class Mapa(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Roomba')
        self.tamanio_mapa = 300  # Tamaño del mapa
        self.ascensor_size = 50  # Tamaño del ascensor
        self.ascensor_visible = False  # Estado del botón del ascensor

        # Coordenadas de la esquina superior derecha del ascensor
        self.ascensor_x = self.tamanio_mapa - self.ascensor_size
        self.ascensor_y = 0

        # Lista de coordenadas de los obstáculos (x, y, ancho, alto)
        self.obstaculos = [(100, 100, 50, 50), (200, 150, 80, 30)]

        self.boton_ascensor = QPushButton('Subir', self)
        self.boton_ascensor.setGeometry(self.ascensor_x, self.ascensor_y, self.ascensor_size, 30)
        self.boton_ascensor.setVisible(False)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)

        # Dibujar mapa
        painter.drawRect(50, 50, self.tamanio_mapa, self.tamanio_mapa)

        # Dibujar obstáculos
        painter.setBrush(QBrush(Qt.blue))
        for obstaculo in self.obstaculos:
            painter.drawRect(*obstaculo)

        # Dibujar zona del ascensor
        painter.setBrush(QBrush(Qt.green))
        painter.drawRect(self.ascensor_x, self.ascensor_y, self.ascensor_size, self.ascensor_size)

    def mousePressEvent(self, event):
        # Verificar si el clic está dentro de la zona del ascensor
        if QRect(self.ascensor_x, self.ascensor_y, self.ascensor_size, self.ascensor_size).contains(event.pos()):
            self.ascensor_visible = True
            self.boton_ascensor.setVisible(True)
        else:
            self.ascensor_visible = False
            self.boton_ascensor.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mapa = Mapa()
    mapa.show()
    sys.exit(app.exec_())
