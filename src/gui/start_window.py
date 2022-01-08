from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread
from ..solver.SolverFactory import SolverFactory
from ..solver.SolverInterface import ISolver
from .ressource.logo import *


puzzles = ['8-Puzzle', '24-Puzzle', '20-Queens problem', '1000000-Queens problem']
strategies = ['Uninformed search', 'Informed search', 'Local search algorithm']

class StartWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(StartWindow, self).__init__()
        uic.loadUi('./src/gui/template/start_window.ui', self)

        self.puzzle_select          : QtWidgets.QComboBox   = self.findChild(QtWidgets.QComboBox, 'puzzle_select')
        self.strategy_select        : QtWidgets.QComboBox   = self.findChild(QtWidgets.QComboBox, 'strategy_select')
        self.show_metrics_checkbox  : QtWidgets.QCheckBox   = self.findChild(QtWidgets.QCheckBox, 'show_metrics_checkbox')
        self.start_button           : QtWidgets.QPushButton = self.findChild(QtWidgets.QPushButton, 'right_button_spacer')

        self.puzzle         : int           = 0
        self.strategy       : int           = 0 
        self.show_metrics   : bool          = False
        self.solver_factory : SolverFactory = SolverFactory()
        self.solver_thread  : QThread       = None
        self.solver         : ISolver       = None

        self.puzzle_name    : list[str]     = list(self.solver_factory.solvers.keys())
        self.strategy_name  : list[str]     = self.solver_factory.solvers[self.puzzle_name[self.puzzle]]

        self.puzzle_select.addItems(self.puzzle_name)
        self.strategy_select.addItems(self.strategy_name)


        self.start_button.clicked.connect(self.launch_solver)
        self.puzzle_select.currentIndexChanged.connect(self.set_puzzle)
        self.strategy_select.currentIndexChanged.connect(self.set_strategy)
        self.show_metrics_checkbox.stateChanged.connect(self.set_show_metrics)


    def _build_thread(self):
        self.solver_thread  = QThread()
        self.solver         = self.solver_factory.build_solver(self.strategy_name[self.strategy])
        
        self.solver.moveToThread(self.solver_thread)
        self.solver_thread.started.connect(self.solver.start)
        self.solver.finished.connect(self.solver_thread.quit)
        self.solver.finished.connect(self.solver.deleteLater)
        self.solver_thread.finished.connect(self.solver_thread.deleteLater)
        # self.solver.progress.connect(self.reportProgress)

    def launch_solver(self):
        if self.solver_thread is not None:
            return
        self._build_thread()
        self.solver_thread.start()
    
    def set_puzzle(self, index: int) -> None:
        self.puzzle = index
        self.strategy_name = self.solver_factory.solvers[self.puzzle_name[self.puzzle]]
        
        self.set_strategy(0)
        self.strategy_select.clear() 
        self.strategy_select.addItems(self.strategy_name)
    
    def set_strategy(self, index: int) -> None:
        self.strategy = index
    

    def set_show_metrics(self, show_metrics: int) -> None:
        self.show_metrics = True if show_metrics == 2 else False