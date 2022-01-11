from src.solver.grille_solver.a_star.AStar import AStar
from src.solver.grille_solver.GrilleSolver import GrilleSolver
from src.utils.Board import Board

# def new_board_and_solver(N):
#     b = Board('grille', N)
#     for piece in b.pieces:
#         print(piece.id, piece.position)
#     grille = GrilleSolver("grille", N)
#     input_list = grille.board.get_board_list()
#     return AStar(input_list), input_list

# s, input_list = new_board_and_solver(3)
# print(s.solvable(input_list))

# while not s.solvable(input_list):
#     s, input_list = new_board_and_solver(3)
#     print(s.solvable(input_list))

s = AStar(3)

solution_metrics = s.a_star_search()
print("path_to_goal: " + str(solution_metrics.path_to_goal))
print("cost_of_path: " + str(solution_metrics.cost_of_path()))
print("nodes_expanded: " + str(solution_metrics.nodes_expanded))
print("fringe_size: " + str(solution_metrics.fringe_size()))
print("max_fringe_size: " + str(solution_metrics.max_fringe_size))
print("search_depth: " + str(solution_metrics.search_depth))
print("max_search_depth: " + str(solution_metrics.max_search_depth))
print("running_time: " + str(solution_metrics.search_time) + "ms")
print("max_ram_useage: " + str(solution_metrics.max_ram_useage) + "%")