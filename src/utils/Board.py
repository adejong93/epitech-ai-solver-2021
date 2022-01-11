from .Piece import Piece
import random
import math
from src.solver.grille_solver.a_star import grid

class Board:
    def __init__(self,
                 type   : str,
                 size   : int) -> None:
        self.type   : str           = type
        self.size   : int           = size
        self.pieces : list[Piece]   = []
        
        self._init_pieces()

    def solvable_grid(self):
        if self.pieces == []: return False
        # solvability depends on the width...
        width = int(math.sqrt(len(self.get_board_list())))

        # ..whether the row that zero is on is odd/even
        temp_grid = grid.Grid(self.get_board_grid()) # TODO: sort this list/grid confusion

        zero_location = temp_grid.locate_tile(0, temp_grid.state)
        if zero_location[0] % 2 == 0: y_is_even = True
        else: y_is_even = False

        # .. and the number of 'inversions' (not counting '0')

        # strip the blank tile
        input_list = [number for number in self.get_board_list() if number != 0]

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

    def _init_pieces_grille(self) -> None:
        while not self.solvable_grid():
            arrPos = []
            for x in range(self.size):
                for y in range(self.size):
                    arrPos.append((x, y))
            for id in range((self.size ** 2) - 1):
                index = random.randint(0, len(arrPos) - 1)
                self.pieces.append(Piece(id + 1, arrPos.pop(index)))
            return None
    
    def get_board_list(self):
        input_list = [0] * self.size ** 2
        for piece in self.pieces:
            input_list[piece.position[0] * self.size + piece.position[1]] = piece.id
        return input_list

    def get_board_grid(self):
        """Take a list of length n^2, return a nxn 2D list"""        

        board_list = self.get_board_list()

        n = int(math.sqrt(len(board_list)))

        # initialise empty grid
        input_grid = [['-' for x in range(n)] for y in range(n)]

        # populate grid with tiles
        i = 0
        j = 0
        for tile in board_list:
            input_grid[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1

        return input_grid

    def _init_pieces_queen(self) -> None:
        arrPos = []
        for x in range(self.size):
            for y in range(self.size):
                arrPos.append((x, y))
        for _ in range((self.size ** 2) - 1):
            self.pieces.append(Piece(0, arrPos.pop(0)))

    def _init_pieces(self) -> None:
        return getattr(self, '_init_pieces_' + self.type.lower())()
    
    @staticmethod
    def grille_to_board(grille: list[list[str]]):
        b = Board('queen', len(grille))
        b.pieces = []
        for x in range(b.size):
            for y in range(b.size):
                b.pieces.append(Piece(grille[x][y], (x,y)))
        return b