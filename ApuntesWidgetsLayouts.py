import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox, QRadioButton, QSlider
)
from PySide6.QtCore import Qt

class ApuntesWidgetsLayouts(QMainWindow):
    """
    Clase que sirve como apunte visual y funcional de los widgets y layouts
    esenciales.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apuntes de Widgets y Layouts Esenciales")

        # 1. ESTABLECER EL WIDGET CENTRAL Y EL LAYOUT MAESTRO (Vertical)
        # QWidget es el contenedor de todos los demás elementos.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # El layout principal organiza todo en vertical (QVBoxLayout)
        main_layout = QVBoxLayout(central_widget)

        # -------------------------------------------------------------------
        ## A. WIDGETS DE ENTRADA Y SALIDA (QWidgets)
        # -------------------------------------------------------------------

        main_layout.addWidget(QLabel("--- WIDGETS DE TEXTO Y ETIQUETAS ---"))

        # QLabel: Para mostrar texto. No es interactivo.
        self.etiqueta_nombre = QLabel("Nombre:")

        # QLineEdit: Para que el usuario inserte una sola línea de texto (entrada).
        self.entrada_nombre = QLineEdit()
        self.entrada_nombre.setPlaceholderText("Introduce tu nombre...") # Texto guía

        # Usamos un QHBoxLayout para poner la etiqueta y el campo de texto al lado
        layout_nombre = QHBoxLayout()
        layout_nombre.addWidget(self.etiqueta_nombre)
        layout_nombre.addWidget(self.entrada_nombre)
        main_layout.addLayout(layout_nombre)

        # -------------------------------------------------------------------
        ## B. LAYOUTS: ORGANIZACIÓN HORIZONTAL Y GRIDS
        # -------------------------------------------------------------------

        main_layout.addWidget(QLabel("\n--- LAYOUTS (Organización de Elementos) ---"))

        # QHBoxLayout: Organiza elementos en línea (horizontal)
        layout_botones = QHBoxLayout()
        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        layout_botones.addWidget(self.btn_aceptar)
        layout_botones.addWidget(self.btn_cancelar)
        main_layout.addLayout(layout_botones) # Añadimos la fila de botones al layout principal

        # QGridLayout: Organiza elementos en tablas (filas y columnas)
        main_layout.addWidget(QLabel("\n--- QGridLayout (Fila, Columna) ---"))
        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel("Fila 0, Col 0"), 0, 0)
        grid_layout.addWidget(QLabel("Fila 0, Col 1"), 0, 1)
        grid_layout.addWidget(QLabel("Fila 1, Col 0"), 1, 0)
        grid_layout.addWidget(QLabel("Fila 1, Col 1"), 1, 1)

        main_layout.addLayout(grid_layout)

        # -------------------------------------------------------------------
        ## C. WIDGETS DE SELECCIÓN (Checkbox, RadioButton, Slider)
        # -------------------------------------------------------------------

        main_layout.addWidget(QLabel("\n--- WIDGETS DE SELECCIÓN ---"))

        # QCheckBox: Selección múltiple (se pueden marcar varios)
        self.check_opcion1 = QCheckBox("Permiso 1")
        self.check_opcion2 = QCheckBox("Permiso 2")

        # QRadioButton: Selección exclusiva (solo se puede marcar uno)
        self.radio_opcionA = QRadioButton("Opción A")
        self.radio_opcionB = QRadioButton("Opción B")

        layout_seleccion = QHBoxLayout()
        layout_seleccion.addWidget(self.check_opcion1)
        layout_seleccion.addWidget(self.check_opcion2)
        layout_seleccion.addWidget(self.radio_opcionA)
        layout_seleccion.addWidget(self.radio_opcionB)
        main_layout.addLayout(layout_seleccion)

        # QSlider: Permite seleccionar un valor en un rango (longitud de contraseña)
        main_layout.addWidget(QLabel("\nQSlider (Control Deslizante):"))
        self.slider_valor = QSlider(Qt.Horizontal)
        self.slider_valor.setMinimum(1)
        self.slider_valor.setMaximum(100)
        self.slider_valor.setValue(50)
        main_layout.addWidget(self.slider_valor)

        # -------------------------------------------------------------------
        ## D. CONEXIÓN DE SEÑALES Y SLOTS (Interactividad)
        # -------------------------------------------------------------------

        self.etiqueta_estado = QLabel("Aún no has presionado nada.")
        main_layout.addWidget(self.etiqueta_estado)

        # Ejemplo de conexión: Cuando se pulsa el botón Aceptar, llama al método 'saludar'
        self.btn_aceptar.clicked.connect(self.saludar)

        # Ejemplo de conexión: Cuando el valor del slider cambia, llama al método 'actualizar_slider'
        self.slider_valor.valueChanged.connect(self.actualizar_slider)


    # --- SLOTS (Métodos que Responden a las Señales) ---

    def saludar(self):
        """ Responde a la señal 'clicked' del botón 'Aceptar'. """
        nombre = self.entrada_nombre.text()
        if nombre:
            self.etiqueta_estado.setText(f"¡Hola, {nombre}! Botón Aceptar presionado.")
        else:
            self.etiqueta_estado.setText("Por favor, introduce un nombre.")

    def actualizar_slider(self, valor):
        """ Responde a la señal 'valueChanged' del slider. """
        self.etiqueta_estado.setText(f"Slider movido a: {valor}")


# 3. BUCLE DE EJECUCIÓN
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ApuntesWidgetsLayouts()
    ventana.show()
    sys.exit(app.exec())