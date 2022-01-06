from PyQt5 import QtWidgets, uic


puzzles = ['8-Puzzle', '24-Puzzle', '20-Queens problem', '1000000-Queens problem']
strategies = ['Uninformed search', 'Informed search', 'Local search algorithm']

class StartWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(StartWindow, self).__init__()
        uic.loadUi('./src/gui/template/start_window.ui', self)

        self.puzzle_select = self.findChild(QtWidgets.QComboBox, 'puzzle_select')
        self.strategy_select = self.findChild(QtWidgets.QComboBox, 'strategy_select')
        self.show_metrics_checkbox = self.findChild(QtWidgets.QCheckBox, 'show_metrics_checkbox')

        self.puzzle = 0
        self.strategy = 0 
        self.show_metrics = False

        self.puzzle_select.addItems(puzzles)
        self.strategy_select.addItems(strategies)

        self.puzzle_select.currentIndexChanged.connect(self.set_puzzle)
        self.strategy_select.currentIndexChanged.connect(self.set_strategy)
        self.show_metrics_checkbox.stateChanged.connect(self.set_show_metrics)

        self.show()
    
    
    def set_puzzle(self, index):
        self.puzzle = index

    
    def set_strategy(self, index):
        self.strategy = index
    

    def set_show_metrics(self, show_metrics):
        self.show_metrics = True if show_metrics == 2 else False