
# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Desarrollado Por: Cristian M. Veliz Cano
Verción del Soft: V-02
Nombre del Soft: Emojis - Python-WhatsApp

EN MEGA:
https://mega.nz/file/PxsggLjb#EWpdgaBfhN0fLBU8d659f7val3asEt-_kmt21AOK-EM
'''
##-----------------------------------------------------------------------------------------
# --- IMPORTS ---
##-----------------------------------------------------------------------------------------
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, QMenuBar, QMessageBox)
from PyQt5.QtGui import QIcon, QFontDatabase, QFont
from PyQt5.QtCore import Qt
##-----------------------------------------------------------------------------------------
import sys
import os
from Unicode_Emojis import emojis_generales

##-----------------------------------------------------------------------------------------
# --- CLASE PARA MANEJO DE RUTAS ---
##-----------------------------------------------------------------------------------------
class PathManager:
    """Gestiona las rutas de la aplicación, tanto en desarrollo como en el ejecutable de PyInstaller."""
    @staticmethod
    def get_base_path():
        """Obtiene el directorio base donde se ejecuta la aplicación."""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return base_path

    @staticmethod
    def get_resource_path(relative_path):
        """Obtiene la ruta absoluta a un recurso, funciona en desarrollo y con PyInstaller."""
        return os.path.join(PathManager.get_base_path(), relative_path)

##-----------------------------------------------------------------------------------------
# --- CLASE PRINCIPAL (VENTANA) ---
##-----------------------------------------------------------------------------------------
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Guardamos el contenido original en una variable para poder recargarlo
        self.emojis_originales = emojis_generales

        # Llamamos a un método para organizar la inicialización de la UI
        self.init_ui()

    # --Creamos en el (init_ui), el StyleSheet [Hoja de Estilo], Para que Adopte el Modo Matrix...
    def init_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: #00ff41;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 11px;
            }
            
            QTextEdit {
                background-color: #0a0a0a;
                color: #00ff41;
                border: 1px solid #00c3ff;
                border-radius: 6px;
                font-family: 'Consolas', monospace;
                padding: 10px;
                font-size: 20px;
            }
            
            QScrollBar:vertical {
                background-color: #0a0a0a;
                width: 12px;
                border: 1px solid #00c3ff;
            }
            
            QScrollBar::handle:vertical {
                background-color: #00c3ff;
                border-radius: 6px;
                min-height: 20px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #80ff00;
            }
        """)

        """Inicializa todos los componentes de la interfaz de usuario."""
        # 1. Propiedades de la Ventana Principal
        self.setWindowTitle("Emojis - Python-WhatsApp_v2")
        self.Ico_app = PathManager.get_resource_path('Ico\\1.Ico')
        self.setWindowIcon(QIcon(self.Ico_app))
        self.center_on_screen()

        # 2. Crear la Barra de Menús y sus acciones
        self.crear_menu()

        # 3. Crear el Widget Central (QTextEdit)
        self.Emojins = QTextEdit(self)
        self.setCentralWidget(self.Emojins)
        self.Emojins.setReadOnly(True)
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        #self.Emojins.setFont(fixedfont)
        #self.Emojins.setLineWrapMode(QTextEdit.NoWrap)
        self.Emojins.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Emojins.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Emojins.setAcceptRichText(True)              
        self.Emojins.setFont(QFont("Consolas", 9))

        # 4. Cargar el contenido inicial
        self.cargar_emojis()

    # --- Función Cargar Modo NORMAL ---
    def QtextxtEdit_Normal(self):

        self.Emojins.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #F1F1F1;
                border: 1px solid #5A5A5A;
                border-radius: 6px;
                font-family: 'Consolas', monospace;
                padding: 10px;
                font-size: 15pt;
            }
        """)

    # --- Función Cargar Modo MATRIX ---
    def QtextxtEdit_MATRIX(self):

        self.Emojins.destroy()

        # Create a text edit to display the output
        self.Emojins = QTextEdit(self)
        self.setCentralWidget(self.Emojins)
        self.Emojins.setReadOnly(True)
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.Emojins.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Emojins.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Emojins.setAcceptRichText(True)              
        self.Emojins.setFont(QFont("Consolas", 9))

        # 4. Cargar el contenido inicial
        self.cargar_emojis()

    def crear_menu(self):
        """Crea la barra de menús y añade las acciones."""
        # Crear la barra de menús
        barra_menu = self.menuBar()
        barra_menu.setStyleSheet('''
            QMenuBar {border:5px solid #000;}
            QMenuBar::item::selected{background-color:#008000}           
            QMenu::item::selected {background-color: #400080}
            ''')

        # Crear el menú "Archivo"   QMenu {background-color: #2d2d30; color: white;}
        menu_archivo = barra_menu.addMenu("Archivo")

        # --- Función No. 1: Cargar de Nuevo ---
        accion_cargar = QAction("Cargar de Nuevo", self)
        accion_cargar.setShortcut("Ctrl+R") # Atajo de teclado opcional
        accion_cargar.setStatusTip("Vuelve a cargar la lista completa de emojis") # Mensaje en la barra de estado
        accion_cargar.triggered.connect(self.cargar_emojis) # Conectar la acción con el método
        menu_archivo.addAction(accion_cargar)

        # Añadir un separador visual
        menu_archivo.addSeparator()

        # --- Función No. 2: Salir ---
        accion_salir = QAction("Salir", self)
        accion_salir.setShortcut("ESC") # Atajo de teclado estándar
        accion_salir.setStatusTip("Salir de la aplicación")
        accion_salir.triggered.connect(self.salir) # Conectar la acción con el método
        menu_archivo.addAction(accion_salir)
        
        # Crear el menú "Archivo"
        menu_QTextEdit = barra_menu.addMenu("Ventana de Texto")

        # --- Función No. 1: Cargar de Nuevo ---
        text_edit = QAction("Ventana de Texto Normal?", self)
        text_edit.setShortcut("Ctrl+N") # Atajo de teclado opcional
        text_edit.setStatusTip("Ver ventana de emojis en Texto Blanco|Negro") # Mensaje en la barra de estado
        text_edit.triggered.connect(self.QtextxtEdit_Normal) # Conectar la acción con el método
        menu_QTextEdit.addAction(text_edit)

        # Añadir un separador visual
        menu_QTextEdit.addSeparator()

        # --- Función No. 1: Cargar de Nuevo ---
        text_edit_m = QAction("Ventana de Texto (MATRIX)?", self)
        text_edit_m.setShortcut("Ctrl+M") # Atajo de teclado opcional
        text_edit_m.setStatusTip("Ver ventana de emojis en tipo [MATRIX]") # Mensaje en la barra de estado
        text_edit_m.triggered.connect(self.QtextxtEdit_MATRIX) # Conectar la acción con el método
        menu_QTextEdit.addAction(text_edit_m)

    def cargar_emojis(self):
        """Carga el texto original de los emojis en el QTextEdit."""
        self.Emojins.setText(self.emojis_originales)
        self.statusBar().showMessage("Emojis recargados.", 3000) # Mensaje temporal en la barra de estado

    def salir(self):
        """Cierra la aplicación."""
        self.close()

    def center_on_screen(self):
        """Centra la ventana en la pantalla."""
        screen = QApplication.primaryScreen().availableGeometry()
        w, h = 775, 445
        x = (screen.width() - w) // 2
        y = (screen.height() - h) // 2 + 10
        self.setGeometry(x, y, w, h)

##-----------------------------------------------------------------------------------------
# --- BLOQUE DE EJECUCIÓN PRINCIPAL ---
##-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Fuente monoespaciada global
    font = QFont("Consolas", 10)
    font.setStyleHint(QFont.Monospace)
    app.setFont(font)

    w = Ventana()
    w.show()
    sys.exit(app.exec_())