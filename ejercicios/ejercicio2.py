import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QMainWindow

class VentanaClave(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Ingreso de Clave Secreta")
        self.setGeometry(100, 100, 300, 150)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        etiqueta = QLabel("Ingrese su clave:", self)
        self.clave = QLineEdit(self)
        self.clave.setEchoMode(QLineEdit.Password)

        layout.addWidget(etiqueta)
        layout.addWidget(self.clave)

        central_widget.setLayout(layout)

if _name_ == "_main_":
    app = QApplication(sys.argv)
    ventana = VentanaClave()
    ventana.show()
    sys.exit(app.exec_())