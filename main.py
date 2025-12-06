import time
import copy
"""
Sudoku Solve using Uniformed Search Techniques
Uses BFS and DFS to solve the sudoku puzzles
Tracks Game States and Performance Metrics
"""
"""
-should utilise appropriate data structures to allow efficient and 
low consumption of memory on your computer
-Use descriptive statistics
"""


class Sudoku_state:
    """ A class to represent a Sudoku game state """

    def __init__ (self, board, size):
        self.board = board #2d List of Sudoku Board
        self.size = size #Size of Grid(4, 9 or 16)
        self.box_size= int(size ** 0.5) # The Size of each box

    def __hash__(self):
        """Makes the state hashable so that it 
        can be used in sets and as dictionary keys"""
        
        return hash(str(self.board))
    
    def __eq__(self, other):
        """Checks the equality for a set"""

        return self.board == other.board
    
    def copy(self):
        """Creates a new copy of the state that is selected"""
        return Sudoku_state([copy.deepcopy((self.board), self.size)])
        pass

    def valid_placement(self, row, col, num):
        """Checks if the placement of num at row, col is a valid move"""

        if num in self.board[row]:
            return False
        if num in [self.board[r][col] for r in range(self.size)]:
            return False
        
        #Checking the Box
        box_row_start= row - row % self.box_size
        box_col_start= col - col % self.box_size

        for r in range(box_row_start, box_row_start + self.box_size):
            for c in range(box_col_start, box_col_start + self.box_size):
                if self.board[r][c]== num:
                    return False
                
        return True


    def find_empty_cell(self):
        """Finds the first empty cell on the board
        Checks if it contains a 0, which represents if a cell is empty
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col]==0:
                    return (row, col)
        
        #Automatically returns None if no empty cells are found
        return None

    def is_goal_satate(self):
        """Checks if this state is the same as the goal state (i.e if its solved) 
        All Cellls MUST be filled"""

        return self.find_empty_cell() is None


    def get_successor(self):
        """ Generate all the valid possible sucessor states"""

        sucessors=[]
        empty_cell=self.find_empty_cell()

        if empty_cell is None:
            return sucessors
        
        row, col = empty_cell
        #Tries all possible Numbers in the empty cell
        for num in range (1, self.size+1):
            if self.valid_placement(row,col,num):

                new_state= self.copy()
                new_state.board[row][col]=num
                sucessors.append(new_state)


        return sucessors

    def display(self):
        """Displays the Sudoku Board, making it easily readable"""
        pass
    


