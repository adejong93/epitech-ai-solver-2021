from abc import abstractmethod
from ..utils.Board import Board

from PyQt5.QtCore import QObject, pyqtSignal
from ..utils.metric import Metric

class ISolver(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def __init__(self,
                 type   : str,
                 size   : int) -> None:
        self.type   = type
        self.size   = size
        self.board  = Board(self.type, self.size)
        self.metric = Metric()
        super().__init__()

    @abstractmethod
    def start(initState : Board):
        raise NotImplementedError