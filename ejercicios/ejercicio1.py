import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow

class VentanaInformacion(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Información")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.label_info = QLabel("Nombre: Juan Pérez\nEdad: 25 años", self)

        layout.addWidget(self.label_info)

        central_widget.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    ventana = VentanaInformacion()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "_main_":
    main()