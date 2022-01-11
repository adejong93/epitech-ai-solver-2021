from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread
from .ressource.logo import *
from ..solver.SolverInterface import ISolver


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, solver: ISolver) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi('./src/gui/template/main_window.ui', self)
    
        self.current_state_view     : QtWidgets.QGridLayout = self.findChild(QtWidgets.QGridLayout, 'current_state_view')
        self.solver                 : ISolver               = solver
        self.solver_thread          : QThread               = QThread()

        board = self.solver.board.get_board_grid()
        print("BOARD =>")
        print(board)
        print(self.solver.board.solvable_grid())

        for y in range(0, self.solver.board.size):
            for x in range(0, self.solver.board.size):
                label:  QtWidgets.QLabel = QtWidgets.QLabel(None)

                label.setText(str(board[y][x]))
        self._build_thread()
        self.solver_thread.start()

    def _build_thread(self):
        self.solver_thread  = QThread()
        
        self.solver.moveToThread(self.solver_thread)
        self.solver_thread.started.connect(self.solver.start)
        self.solver.finished.connect(self.solver_thread.quit)
        self.solver.finished.connect(self.solver.deleteLater)
        self.solver.finished.connect(self._solver_finished)
        self.solver_thread.finished.connect(self.solver_thread.deleteLater)
    
    def _solver_finished(self):
        self.metric = self.solver.metric
        if self.solver.type == "grille":
            self.metric.from_path_to_goal_list(self.solver.board.get_board_grid())
        # print(self.metric.path_to_goal_list)
