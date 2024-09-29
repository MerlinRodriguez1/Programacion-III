import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow, QDateEdit
from PyQt5.QtCore import QDate

class VentanaSeleccionFecha(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Selector de Fecha")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.etiqueta = QLabel("Seleccione una fecha:", self)
        self.fecha = QDateEdit(self)
        self.fecha.setCalendarPopup(True)
        self.fecha.setDate(QDate.currentDate())
        self.fecha.dateChanged.connect(self.mostrar_fecha)

        layout.addWidget(self.etiqueta)
        layout.addWidget(self.fecha)

        central_widget.setLayout(layout)

    def mostrar_fecha(self):
        fecha_seleccionada = self.fecha.date().toString("dd/MM/yyyy")
        self.etiqueta.setText(f"Fecha seleccionada: {fecha_seleccionada}")

def main():
    app = QApplication(sys.argv)
    ventana = VentanaSeleccionFecha()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "_main_":
    main()