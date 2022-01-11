from .SolverInterface import ISolver

from .queen_solver import (
    HillClimbSolver,
    BackTrackingSolver
)

from .grille_solver.BranchAndBound import GrilleBranchAndBound
from .grille_solver.a_star.AStar import AStar

class SolverFactory:
    def __init__(self) -> None:
        self.solvers : dict[str, list[str]] = {
            'grille' : ['AStar'],
            'queen': ['BackTracking']
        }
        self.problems: dict[str, list[str]] = {
            'grille': ['8-Puzzle', '24-Puzzle'],
            'queen': ['20-Queens problem', '1000000-Queens problem']
        }
        self.problems_list: list[str] = [item for sublist in list(self.problems.values()) for item in sublist]

        self.HillClimbSolver        : HillClimbSolver       = HillClimbSolver
        self.BackTracking           : BackTrackingSolver    = BackTrackingSolver

        self.GrilleBranchAndBound   : GrilleBranchAndBound  = GrilleBranchAndBound
        self.AStar                  : AStar                 = AStar
    
    def build_solver(self,
                     solver_name    : str,
                     size           : int,
                     ) -> ISolver:
        return getattr(self, solver_name)(size)