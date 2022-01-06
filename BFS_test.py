from src.solver.grille_solver.GrilleSolver import GrilleSolver
from src.utils.Board import Board
from src.solver.grille_solver.GrilleSolver import GrilleSolver
from src.solver.grille_solver.pynpuzzle.breadth_first_tree_search import a_star_manhattan_heuristic_search


b = Board('grille', 3)
for piece in b.pieces:
    print(piece.id, piece.position)
grille = GrilleSolver(3)
initial, goal = grille.get_initial_goal(b)
print(initial)
print(goal)
output = a_star_manhattan_heuristic_search(initial, goal)
print("OUTPUT")
print(output)