from PyQt5 import QtWidgets, uic
from .ressource.logo import *


puzzles = ['8-Puzzle', '24-Puzzle', '20-Queens problem', '1000000-Queens problem']
strategies = ['Uninformed search', 'Informed search', 'Local search algorithm']

class StartWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(StartWindow, self).__init__()
        uic.loadUi('./src/gui/template/start_window.ui', self)

        self.puzzle_select          : QtWidgets.QComboBox = self.findChild(QtWidgets.QComboBox, 'puzzle_select')
        self.strategy_select        : QtWidgets.QComboBox = self.findChild(QtWidgets.QComboBox, 'strategy_select')
        self.show_metrics_checkbox  : QtWidgets.QCheckBox = self.findChild(QtWidgets.QCheckBox, 'show_metrics_checkbox')

        self.puzzle         : int = 0
        self.strategy       : int = 0 
        self.show_metrics   : bool = False


        self.puzzle_select.addItems(puzzles)
        self.strategy_select.addItems(strategies)

        self.puzzle_select.currentIndexChanged.connect(self.set_puzzle)
        self.strategy_select.currentIndexChanged.connect(self.set_strategy)
        self.show_metrics_checkbox.stateChanged.connect(self.set_show_metrics)

    
    def set_puzzle(self, index: int) -> None:
        self.puzzle = index

    
    def set_strategy(self, index: int) -> None:
        self.strategy = index
    

    def set_show_metrics(self, show_metrics: int) -> None:
        self.show_metrics = True if show_metrics == 2 else False