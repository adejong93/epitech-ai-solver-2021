from ..SolverInterface import ISolver

class QueenSolver(ISolver):

    def queenCanMove(self, Pieces):
        ...
    
    def get_N_empty_grid(self, N):
        return [[ 0 for i in range(N)] for j in range(N)]
