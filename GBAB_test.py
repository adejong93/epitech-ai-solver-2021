from src.utils.Board import Board
from src.solver.grille_solver.BranchAndBound import GrilleBranchAndBound

b = Board('grille', 3)
for piece in b.pieces:
    print(piece.id, piece.position)
grille = GrilleBranchAndBound(3)
initial, goal = grille.get_initial_goal()
grille.start(b)
