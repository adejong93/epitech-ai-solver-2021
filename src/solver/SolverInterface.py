from abc import abstractmethod
from ..utils.Board import Board

class ISolver:

    @abstractmethod
    def start(initState : Board):
        raise NotImplementedError