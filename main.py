import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setText("NOS VAMOS DE ROOMBA!")
   textLabel.move(110,85)

   widget.setGeometry(150,150,320,200)
   widget.setWindowTitle("Roombaa Time")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()