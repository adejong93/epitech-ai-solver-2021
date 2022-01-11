from src.utils.Board import Board
from ..SolverInterface import ISolver
from src.solver.grille_solver.a_star import grid
import math

class GrilleSolver(ISolver):
    
    def get_initial_goal(self, board: Board):
        initial = [[ 0 for i in range(self.size)] for j in range(self.size)]
        for piece in board.pieces:
            initial[piece.position[0]][piece.position[1]] = piece.id
        # TODO : goal dynamic
        goal = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]
        return initial, goal
