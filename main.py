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
        """
        Docstring for __init__
        
        :param self: Description
        :param board: Description
        :param size: Description
        """
        self.board = board #2d List of Sudoku Board
        self.size = size #Size of Grid(4, 9 or 16)
        self.box_size= int(size ** 0.5) # The Size of each box

    def __hash__(self):
        """
        Docstring for __hash__
        Makes the state hashable so that it 
        can be used in sets and as dictionary keys
        
        :param self: Description
        :return: Description
        :rtype: int
        """
        
        return hash(str(self.board))
    
    def __eq__(self, other):
        """
        Docstring for __eq__
        
        :param self: Description
        :param other: Description
        :return: Description
        :rtype: Any
        """

        return self.board == other.board
    
    def copy(self):
        """
        Docstring for copy
        Creates a new copy of the state that is selected
        :param self: Description
        :return: Description
        :rtype: Sudoku_state
        """
        return Sudoku_state([copy.deepcopy((self.board), self.size)])
        pass

    def valid_placement(self, row, col, num):
        """
        Docstring for valid_placement
        Checks if the placement of num at row, col is a valid move"
        :param self: Description
        :param row: Description
        :param col: Description
        :param num: Description
        """""

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
        """
        Docstring for find_empty_cell
        Finds the first empty cell on the board
        Checks if it contains a 0, which represents if a cell is empty
        :param self: Description
        :return: Description
        :rtype: tuple[int, int] | None
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col]==0:
                    return (row, col)
        
        #Automatically returns None if no empty cells are found
        return None

    def is_goal_state(self):
        """
        Docstring for is_goal_state
        Checks if this state is the same as the goal state (i.e if its solved) 
        All Cellls MUST be filled
        :param self: Description
        :return: Description
        :rtype: bool
        """

        return self.find_empty_cell() is None


    def get_successor(self):
        """
        Docstring for get_successor
        Generate all the valid possible sucessor states
        :param self: Description
        :return: Description
        :rtype: list
        """

        successor=[]
        empty_cell=self.find_empty_cell()

        if empty_cell is None:
            return successor
        
        row, col = empty_cell
        #Tries all possible Numbers in the empty cell
        for num in range (1, self.size+1):
            if self.valid_placement(row,col,num):

                new_state= self.copy()
                new_state.board[row][col]=num
                successor.append(new_state)


        return successor

    def display(self):
        """
        Docstring for display
        Displays the Sudoku Board, making it easily readable
        :param self: Description
        """

        for i, row in enumerate(self.board):
            if i%self.box_size==0 and i>0:
                print("-"*(self.size*2 + self.box_size -1))
            str_row= ""
            for j, num in enumerate(row):
                if i%self.box_size==0 and j>0:
                    str_row += (str(num) if num !=0 else ".") + " "
            print(str_row)




        pass
    


