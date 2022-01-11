from PyQt5 import QtWidgets, uic
from .ressource.logo import *
from ..solver.SolverInterface import ISolver


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, solver: ISolver) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi('./src/gui/template/main_window.ui', self)
    
        self.current_state_view     : QtWidgets.QGridLayout = self.findChild(QtWidgets.QGridLayout, 'current_state_view')
        self.solver                 : ISolver               = solver

        board = self.solver.get_board_grid():

        for y in range(0, len(board.row)):
            for x in range(0, len(board.row[y])):
                label:  QtWidgets.QLabel = QtWidgets.QLabel(None)

                label.setText(boa)


    def set_board(self, board: Board) -> None:
        ...
