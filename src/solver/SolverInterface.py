from abc import abstractmethod
from ..utils.Board import Board

from PyQt5.QtCore import QObject, pyqtSignal

class ISolver(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    @abstractmethod
    def start(initState : Board):
        raise NotImplementedError