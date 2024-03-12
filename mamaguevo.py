import sys
from PyQt6.QtWidgets import QApplication, QWidget

class wnd(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(1366,765,250,250)
        self.setWindowTitle("ROSSE")
        self.show()

if  __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = wnd() 
    sys.exit(app.exec())