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
            'grille' : ['GrilleBranchAndBound', 'AStar'],
            'queen': ['BackTracking', 'HillClimbSolver']
        }

        self.HillClimbSolver        : HillClimbSolver       = HillClimbSolver
        self.BackTracking           : BackTrackingSolver    = BackTrackingSolver

        self.GrilleBranchAndBound   : GrilleBranchAndBound  = GrilleBranchAndBound
        self.AStar                  : AStar                 = AStar
    
    def build_solver(self,
                     solver_name    : str,
                     size           : int,
                     ) -> ISolver:
        return getattr(self, solver_name)(size)