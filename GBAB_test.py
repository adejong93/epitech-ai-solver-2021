from src.utils.Board import Board
from src.utils.Piece import Piece
from src.solver.grille_solver.GrilleSolver import GrilleSolver
from src.solver.grille_solver.BranchAndBound import GrilleBranchAndBound

b = Board('grille', 3)
for piece in b.pieces:
    print(piece.id, piece.position)
grille = GrilleBranchAndBound(3)
grille.start(b)
