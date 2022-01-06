from .SolverInterface import ISolver

from .queen_solver import (
    HillClimbSolver
)

from .grille_solver import (
    GrilleSolver
)

class SolverFactory:
    def __init__(self) -> None:
        self.solvers = [
            'HillClimbSolver',
            ''
        ]
        self.HillClimbSolver    = HillClimbSolver
    
    def build_solver(self,
                     solver_name    : str,
                     ) -> ISolver:
        return getattr(self, solver_name)()
