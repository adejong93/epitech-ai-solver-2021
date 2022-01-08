from .SolverInterface import ISolver

from .queen_solver import (
    HillClimbSolver,
    BackTrackingSolver
)

from .grille_solver import (
    GrilleBranchAndBound,
    AStar
)

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
                     ) -> ISolver:
        return getattr(self, solver_name)(3)