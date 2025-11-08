import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# 1. Definir a clase da ventá principal
class MinhaVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Primera App PySide") # Título da ventá
        self.setGeometry(100, 100, 400, 200) # (X, Y, Ancho, Alto)

        # Crear un widget simple para mostrar algo
        etiqueta = QLabel("Hola Mundo!", self)

# 2. Iniciar a aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv) # Crea o obxecto da aplicación

    # 3. Crear e mostrar a ventá
    ventana = MinhaVentana()
    ventana.show() # Fai visible a ventá

    # 4. Iniciar o bucle de eventos (o corazón da aplicación)
    sys.exit(app.exec())