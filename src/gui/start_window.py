from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread
from ..solver.SolverFactory import SolverFactory
from ..solver.SolverInterface import ISolver
from .ressource.logo import *
from .main_window import MainWindow


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
        self.size_input            : QtWidgets.QSpinBox    = self.findChild(QtWidgets.QSpinBox, 'size_input')

        self.puzzle         : int           = 0
        self.strategy       : int           = 0 
        self.show_metrics   : bool          = False
        self.size           : int           = 0
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
        self.size_input.valueChanged.connect(self.set_size)
        self.show_metrics_checkbox.stateChanged.connect(self.set_show_metrics)


    
        # self.solver.progress.connect(self.reportProgress)

    def _solver_finished(self):
        print(self.solver.metric.path_to_goal[0].get_board_grid())

    def launch_solver(self):
        self.solver = self.solver_factory.build_solver(self.strategy_name[self.strategy], self.size)
        self.window = MainWindow(self.solver)
        self.window.show()
        self.close()
        # self.solver_thread.start()
    
    def set_puzzle(self, index: int) -> None:
        self.puzzle = index
        self.strategy_name = self.solver_factory.solvers[self.puzzle_name[self.puzzle]]
        
        self.set_strategy(0)
        self.strategy_select.clear() 
        self.strategy_select.addItems(self.strategy_name)
    
    def set_strategy(self, index: int) -> None:
        self.strategy = index
    
    def set_size(self, value: int) -> None:
        self.size = value
    
    def set_show_metrics(self, show_metrics: int) -> None:
        self.show_metrics = True if show_metrics == 2 else False