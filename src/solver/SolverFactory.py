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
        self.problems: dict[str, list[str]] = {
            'grille': ['8-Puzzle', '24-Puzzle'],
            'queen': ['20-Queens problem', '1000000-Queens problem']
        }
        self.problems_list: list[str] = [item for sublist in list(self.problems.values()) for item in sublist]

        self.HillClimbSolver    : HillClimbSolver = HillClimbSolver
        self.BranchAndBound     : BranchAndBound  = BranchAndBound
        self.BackTracking       : BackTracking    = BackTracking
    
    def build_solver(self,
                     solver_name    : str,
                     ) -> ISolver:
        return getattr(self, solver_name)()