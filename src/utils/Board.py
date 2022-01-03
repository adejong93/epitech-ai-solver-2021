from .Piece import Piece
import random

class Board:
    def __init__(self,
                 type   : str,
                 size   : int) -> None:
        self.type   : str           = type
        self.size   : int           = size
        self.pieces : list[Piece]   = []
        
        self._init_pieces()

    def _init_pieces_grille(self) -> None:
        arrPos = []
        for x in range(self.size):
            for y in range(self.size):
                arrPos.append((x, y))
        for id in range((self.size ** 2) - 1):
            index = random.randint(0, len(arrPos) - 1)
            self.pieces.append(Piece(id + 1, arrPos.pop(index)))
        return None
    
    def _init_pieces_queen(self) -> None:
        ...

    def _init_pieces(self) -> None:
        return getattr(self, '_init_pieces_' + self.type.lower())()