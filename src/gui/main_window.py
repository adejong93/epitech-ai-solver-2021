from PyQt5 import QtWidgets, uic
from .ressource.logo import *


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi('./src/gui/template/main_window.ui', self)