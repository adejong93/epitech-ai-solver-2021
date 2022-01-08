from PyQt5 import QtWidgets, uic
from .ressource.logo import *
from ..utils.Board import Board


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, board: Board) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi('./src/gui/template/main_window.ui', self)
    

    def set_board(board: Board) -> None:
        ...