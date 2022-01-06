from src.utils.Board import Board
from ..SolverInterface import ISolver

class GrilleSolver(ISolver):

    def __init__(self,
                 n          : int) -> None:
                 self.size  : int   = n
    
    def get_initial_goal(self, board: Board):
        initial = [[ 0 for i in range(self.size)] for j in range(self.size)]
        for piece in board.pieces:
            initial[piece.position[0]][piece.position[1]] = piece.id
        goal = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]
        return initial, goal