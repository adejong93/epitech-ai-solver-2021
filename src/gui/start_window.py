from PyQt5 import QtWidgets, uic

from .ressource.logo import *
from ..solver.SolverFactory import SolverFactory


class StartWindow(QtWidgets.QWidget):
    def __init__(self, solver_factory: SolverFactory) -> None:
        super(StartWindow, self).__init__()
        uic.loadUi('./src/gui/template/start_window.ui', self)

        self.problem_select         : QtWidgets.QComboBox = self.findChild(QtWidgets.QComboBox, 'problem_select')
        self.solver_select          : QtWidgets.QComboBox = self.findChild(QtWidgets.QComboBox, 'solver_select')
        self.show_metrics_checkbox  : QtWidgets.QCheckBox = self.findChild(QtWidgets.QCheckBox, 'show_metrics_checkbox')

        self.problem        : int = 0
        self.solver         : int = 0 
        self.show_metrics   : bool = False

        self.__solver_factory: SolverFactory = solver_factory

        self.problem_select.addItems(self.__solver_factory.problems_list)
        self.set_problem(0)
        self.set_solver(0)

        self.problem_select.currentIndexChanged.connect(self.set_problem)
        self.solver_select.currentIndexChanged.connect(self.set_solver)
        self.show_metrics_checkbox.stateChanged.connect(self.set_show_metrics)

    
    def set_problem(self, index: int) -> None:
        problem_label = self.__solver_factory.problems_list[index]

        self.problem = index

        for key, problem_list in self.__solver_factory.problems.items():
            if problem_label in problem_list:
                self.solver_select.clear()
                self.solver_select.addItems(self.__solver_factory.solvers[key])
    

    def set_solver(self, index: int) -> None:
        self.solver = index


    def set_show_metrics(self, show_metrics: int) -> None:
        self.show_metrics = True if show_metrics == 2 else False