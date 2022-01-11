from .QueenSolver import QueenSolver
from ...utils.Board import Board

class BackTrackingSolver(QueenSolver):
    def __init__(self, size) -> None:
        super().__init__(size=size, type="queen")
        """ ld is an array where its indices indicate row-col+N-1 
        (N-1) is for shifting the difference to store negative 
        indices """
        self.ld = [0] * (8 * self.size)
        
        """ rd is an array where its indices indicate row+col 
        and used to check whether a queen can be placed on 
        right diagonal or not"""
        self.rd = [0] * (8 * self.size)
        
        """column array where its indices indicates column and 
        used to check whether a queen can be placed in that 
            row or not"""
        self.cl = [0] * (8 * self.size)
    
    """ A utility function to print solution """
    def printSolution(self, board): 
        for i in range(self.size):
            for j in range(self.size):
                print(board[i][j], end = " ")
            print() 
    
    """ A recursive utility function to solve N 
    Queen problem """
    def solveNQUtil(self, board, col): 
        
        """ base case: If all queens are placed
            then return True """
        if (col >= self.size):
            return True
            
        """ Consider this column and try placing
            this queen in all rows one by one """
        for i in range(self.size):
            self.metric.nodes_expanded += 1
            self.metric.measure_ram_useage()
            """ Check if the queen can be placed on board[i][col] """
            """ A check if a queen can be placed on board[row][col].
            We just need to check ld[row-col+n-1] and self.rd[row+coln] 
            where ld and rd are for left and right diagonal respectively"""
            if ((self.ld[i - col + self.size - 1] != 1 and 
                self.rd[i + col] != 1) and self.cl[i] != 1):
                    
                """ Place this queen in board[i][col] """
                board[i][col] = 1
                self.ld[i - col + self.size - 1] = self.rd[i + col] = self.cl[i] = 1
                
                """ recur to place rest of the queens """
                if (self.solveNQUtil(board, col + 1)):
                    return (board, True)
                    
                """ If placing queen in board[i][col] 
                doesn't lead to a solution, 
                then remove queen from board[i][col] """
                board[i][col] = 0 # BACKTRACK 
                self.ld[i - col + self.size - 1] = self.rd[i + col] = self.cl[i] = 0
                
                """ If the queen cannot be placed in
                any row in this colum col then return False """
        return (board, False)
        
    """ This function solves the N Queen problem using 
    Backtracking. It mainly uses solveNQUtil() to 
    solve the problem. It returns False if queens 
    cannot be placed, otherwise, return True and 
    prints placement of queens in the form of 1s. 
    Please note that there may be more than one 
    solutions, this function prints one of the 
    feasible solutions."""
    def start(self):
        self.metric.start_timer()
        self.metric.nodes_expanded = 0
        board, success = self.solveNQUtil(self.board.get_board_grid(), 0)
        if not success:
            print("Solution does not exist")
            return False
        self.metric.path_to_goal.append(Board.grille_to_board(board))
        self.metric.stop_timer()
        self.finished.emit()
        # self.printSolution(board)
        return True
