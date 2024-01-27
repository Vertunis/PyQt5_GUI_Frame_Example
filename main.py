# https://www.youtube.com/watch?v=eD91nE8q8Nk

import sys
import GUI  # Importiert GUI
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox, QLabel
from PyQt5.QtGui import QColor
from functools import partial


#Imports aus anderen .py Skripten
# from modul_1 import function_Beispiel_1

#######################################################
#                   Load your GUI
########################################################
class UI(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)

        #######################################################
        #           Connect Buttons, Text, Widgets etc.
        ########################################################
        # Überschrift
        version ="V.1.0.0"
        self.setWindowTitle(f"Titel {version}") # Fenstertitel

        # Tool Tab
        self.btn_start.clicked.connect(self.function_start)
        self.btn_stop.clicked.connect(self.function_stop)
        self.btn_stop.setEnabled(False) # Button initial deaktivieren

        # Verknüpfung der Buttons mit Argument übergabe
        self.btn_select.clicked.connect(partial(self.function_select, 2)) # über partial kann dem Button eine Funktion mit Argument zugewiesen werden

        # Config Tab
        self.combobox_dict = {'Button_1': None,
                              'Button_2': None}

        self.comboBox.addItems(self.combobox_dict.keys()) # Fügt Kombobox Items aus Dictionary hinzu (nur Keys)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed) # ComboBox-Änderungen verknüpfen

    ########################################################
    #                   Declare Function
    ########################################################
    def function_start(self):

        print("Funktion function_start aktiv")
        self.btn_stop.setEnabled(True) # Button initial deaktivieren

    def function_stop(self):

        print("Funktion function_stop aktiv")

    def function_select(self, arg):

        if arg == 0:
            state = 0
        elif arg == 1:
            state = 1
        elif arg == 2:
            state = 2

        print(rf"Funktion function_select mit Argument: {state} aktiv")

    def on_combobox_changed(self, index):
        # Aktion ausführen, wenn sich die ComboBox ändert (optional)
        selected_key = self.comboBox.currentText()
        selected_value = self.combobox_dict[selected_key]
        print(f"Ausgewählte Option: {selected_key}, Wert: {selected_value}")

#######################################################
#                   Main Function
########################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    PyWindow = UI()
    PyWindow.show()
    app.exec_()