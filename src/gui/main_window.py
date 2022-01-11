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
        self.next_step_button       : QtWidgets.QToolButton = self.findChild(QtWidgets.QToolButton, 'next_state_button')
        self.go_to_end_button       : QtWidgets.QToolButton = self.findChild(QtWidgets.QToolButton, 'go_to_end_button')
        self.reset_button           : QtWidgets.QToolButton = self.findChild(QtWidgets.QToolButton, 'reset_button')
        self.nodes                  : QtWidgets.QLabel      = self.findChild(QtWidgets.QLabel, 'nodes_nb_value_label')
        self.duration               : QtWidgets.QLabel      = self.findChild(QtWidgets.QLabel, 'duration_value_label')
        self.max_search_depth       : QtWidgets.QLabel      = self.findChild(QtWidgets.QLabel, 'max_depth_value_label')
        self.ram                    : QtWidgets.QLabel      = self.findChild(QtWidgets.QLabel, 'ram_value_label')

        self.step                   : int                   = 0

        self._build_thread()
        self.solver_thread.start()

        self.next_step_button.clicked.connect(self._next_step_click)
        self.go_to_end_button.clicked.connect(self._go_to_end_click)
        self.reset_button.clicked.connect(self._reset_click)
    
    def _next_step_click(self):
        if self.step == len(self.metric.path_to_goal_list) - 1:
            return
        self.step += 1
        self._draw_state()

    def _go_to_end_click(self):
        self.step = len(self.metric.path_to_goal_list) - 1
        self._draw_state()
    
    def _reset_click(self):
        self.step = 0
        self._draw_state()
    
    def _draw_state(self):
        board = self.metric.path_to_goal_list[self.step]

        for i in reversed(range(self.current_state_view.count())): 
            self.current_state_view.itemAt(i).widget().setParent(None)

        for y in range(0, self.solver.size):
            for x in range(0, self.solver.size):
                label:  QtWidgets.QLabel = QtWidgets.QLabel(None)

                label.setText(str(board[y][x]))
                self.current_state_view.addWidget(label, y, x)
        
        self.nodes.setText(str(self.metric.nodes_expanded))
        self.duration.setText(str(self.metric.search_time) + 'ms')
        self.max_search_depth.setText(str(self.metric.max_search_depth))
        self.ram.setText(str(self.metric.max_ram_useage) + '%')

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
        print('States:')
        print(self.metric.path_to_goal_list)
        self._draw_state()
