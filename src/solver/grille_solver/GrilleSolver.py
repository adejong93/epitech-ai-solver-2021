from src.utils.Board import Board
from ..SolverInterface import ISolver
from src.solver.grille_solver.a_star import grid
import math

class GrilleSolver(ISolver):

    def __init__(self,
                 n          : int) -> None:
        self.size  : int   = n
        super().__init__()
    
    def get_initial_goal(self, board: Board):
        initial = [[ 0 for i in range(self.size)] for j in range(self.size)]
        for piece in board.pieces:
            initial[piece.position[0]][piece.position[1]] = piece.id
        goal = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]
        return initial, goal
    
    def get_initial_list(self, board: Board):
        input_list = [0] * self.size**2
        for piece in board.pieces:
            input_list[piece.position[0] * 3 + piece.position[1]] = piece.id
        return input_list
    
    def list_to_grid(self, tile_list):
        """Take a list of length n^2, return a nxn 2D list"""        

        # TODO: Shouldn't this be a method of grid instead?

        n = int(math.sqrt(len(tile_list)))

        # initialise empty grid
        input_grid = [['-' for x in range(n)] for y in range(n)]

        # populate grid with tiles
        i = 0
        j = 0
        for tile in tile_list:
            input_grid[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1

        return input_grid
    
    def solvable(self, input_list):
        # solvability depends on the width...
        width = int(math.sqrt(len(input_list)))

        # ..whether the row that zero is on is odd/even
        temp_grid = grid.Grid(self.list_to_grid(input_list)) # TODO: sort this list/grid confusion

        zero_location = temp_grid.locate_tile(0, temp_grid.state)
        if zero_location[0] % 2 == 0: y_is_even = True
        else: y_is_even = False

        # .. and the number of 'inversions' (not counting '0')

        # strip the blank tile
        input_list = [number for number in input_list if number != 0]

        inversion_count = 0
        list_length = len(input_list)

        for index, value in enumerate(input_list):
            for value_to_compare in input_list[index + 1 : list_length]:
                if value > value_to_compare:
                    inversion_count += 1                    
        
        if inversion_count % 2 == 0: inversions_even = True
        else: inversions_even = False

        if width % 2 == 0: width_even = True
        else: width_even = False

        # our zero_location tuple counts rows from the top,
        # but this algorithm needs to count from the bottom
        if width_even:
            zero_odd = not y_is_even
        # if width not even, we don't need zero_odd
        
        return ((not width_even and inversions_even)
                or
                (width_even and (zero_odd == inversions_even)))
