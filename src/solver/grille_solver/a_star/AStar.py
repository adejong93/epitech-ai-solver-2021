from src.solver.grille_solver.GrilleSolver import GrilleSolver
from src.solver.grille_solver.GrilleSolver import GrilleSolver
from . import grid
from . import custom_structures
from ....utils import metric
import copy
import math
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

class AStar(GrilleSolver):

    """Controller class."""
    
    def __init__(self, size):
        super().__init__("grille", size)
        """Initialise Solver object. Raise ValueError if solution not possible."""

        # don't just bind to input state. we want the object to have its OWN state
        self.initial_state = copy.deepcopy(self.board.get_board_grid()) 
        
        self.goal_state = self.set_goal_state(self.board.get_board_list())

        # using custom structures so we can implement a custom __contains__()
        self.frontier = custom_structures.Frontier() 
        self.ast_frontier = custom_structures.Priority_Frontier()       
        self.explored = custom_structures.Explored()

        # TODO: fringe metrics not working for ast (because we're passing it wrong frontier here)
        self.metrics = metric.Metric(self.frontier)


    def uninformed_search(self, search_method):
        """Explore search space using either breadth-first or depth-first search"""

        self.metrics.start_timer()

        initial_grid = grid.Grid(self.initial_state)
        self.frontier.queue.append(initial_grid)
        
        # while queue is not empty..
        while self.frontier.queue:

            # TODO: better name for state. It's a grid. state.state is the state!            
            if search_method == 'bfs':
                state = self.frontier.queue.popleft() 
            elif search_method == 'dfs': 
                state = self.frontier.queue.pop()  
            
            self.metrics.search_depth = len(state.path_history)
            self.metrics.update_max_depth()

            self.explored.set.add(state)

            if self.goal_test(state):
                self.metrics.path_to_goal = state.path_history
                self.metrics.stop_timer()
                self.metrics.measure_ram_useage()                 
                return self.metrics

            self.expand_nodes(state, search_method)

        # if we get to here it's gone tits up
        raise ValueError('Shouldn\'t have got to here - gone tits')

    

    def a_star_search(self):
        """Explore search space using A*-search, using Manhattan Priority
           Function as a heuristic."""

        self.metrics.start_timer()

        initial_grid = grid.Grid(self.initial_state)
        initial_grid.score = initial_grid.manhattan_score(self.goal_state)

        # TODO: ridiculous parameters
        new_item = PrioritizedItem(initial_grid.score, initial_grid)
        self.ast_frontier.queue.put((new_item)) 
        
        # while queue is not empty..
        while self.ast_frontier.queue:

            # TODO: better name for state. It's a grid. state.state is the state!
            lowest_scored = self.ast_frontier.queue.get()
            state = lowest_scored.item
                      
            self.metrics.search_depth = len(state.path_history)
            self.metrics.update_max_depth()

            self.explored.set.add(state)

            if self.goal_test(state):
                self.metrics.path_to_goal = state.path_history
                self.metrics.stop_timer()
                self.metrics.measure_ram_useage()                 
                return self.metrics

            self.expand_nodes(state, 'ast')

        # if we get to here it's gone tits up
        raise ValueError('Shouldn\'t have got to here - gone tits')


    
    def expand_nodes(self, starting_grid, search_method):
        """Take a grid state, add all possible 'next moves' to the frontier"""

        node_order = ['up', 'down', 'left', 'right']

        if search_method == 'dfs':
            node_order = reversed(node_order)

        for node in node_order:   

            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(starting_grid.state)

            # pass path history from previous grid to the next grid
            # using copy to avoid python's reference bindings
            imagined_grid.path_history = copy.copy(starting_grid.path_history)

            if imagined_grid.move(node):  # returns false if move not possible
                
                imagined_grid.path_history.append(node)

                if imagined_grid not in self.frontier and imagined_grid not in self.explored:
                    if search_method == 'ast':
                        imagined_grid.score = imagined_grid.manhattan_score(self.goal_state)
                        item = PrioritizedItem(imagined_grid.score, imagined_grid)
                        self.ast_frontier.queue.put((item))
                    else:
                        self.frontier.queue.append(imagined_grid)               
                        
                    self.metrics.update_max_fringe()

            self.metrics.nodes_expanded += 1

    def goal_test(self, state):
        """Compare a given state to the goal state. Return Boolean"""
        
        # TODO: confusing names. state here is not a Grid.state but a Grid
        if state.state == self.goal_state:
            return True
        else:
            return False

    def set_goal_state(self, input_list):
        """Construct and return a grid state in the correct order."""

        # initialise empty grid state
        n = int(math.sqrt(len(input_list)))
        goal_state = [['-' for x in range(n)] for y in range(n)]

        # populate goal grid with ordered tiles
        i = 0
        j = 0
        count = 1
        
        while i < n:            
            if count == n * n:
                count = 0
            goal_state[i][j] = count
            count += 1      
            j += 1
            if j == n:
                j = 0
                i += 1

        return goal_state

    def start(self):
        self.metric = self.a_star_search()
        self.finished.emit()