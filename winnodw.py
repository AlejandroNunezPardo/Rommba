from PyQt5.QtWidgets import QMainWindow, QApplication 

 

# Definición de una QMainWindow personalizada para poder 

# crear instancias de futuros widgets en ella. 

class MainWindow(QMainWindow): 

  def __init__(self): 

    super(MainWindow, self).__init__() 

 

if __name__ == '__main__': 

 

  # Requisitos para obtener sys.argv. 

  import sys 

 

  # QApplication requiere la lista de argumentos pasadas 

  # al ejecutable durante su instanciación. 

  app = QApplication(sys.argv) 

 

  # Creación de la ventana principal. 

  window = MainWindow() 

 

  # Visualización de la ventana principal. 

  window.show() 

 

  # Inicio del bucle de eventos, cuyo valor 

  # de retorno se utilizará como código de salida de la ejecución. 

  sys.exit(app.exec_())