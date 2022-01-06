from .SolverInterface import ISolver

from .queen_solver import (
    BackTracking,
    HillClimbSolver
)

from .grille_solver import (
    BranchAndBound,
    GrilleSolver
)

class SolverFactory:
    def __init__(self) -> None:
        self.solvers : dict[str, list[str]] = {
            'grille': ['BranchAndBound'],
            'queen': ['BackTracking', 'HillClimbSolver']
        }

        self.HillClimbSolver    : HillClimbSolver = HillClimbSolver
        self.BranchAndBound     : BranchAndBound  = BranchAndBound
        self.BackTracking       : BackTracking    = BackTracking
    
    def build_solver(self,
                     solver_name    : str,
                     ) -> ISolver:
        return getattr(self, solver_name)()