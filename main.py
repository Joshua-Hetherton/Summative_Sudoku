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
import time

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
        "Checks the equality for a set"

        return self.board == other.board
    
    def copy(self):
        pass

    def valid_placement(self, row, col, num):
        pass

    def find_empty_cell(self):
        pass

    def is_goal_satate(self):
        pass

    def get_successor(self):
        pass

    def display(self):
        pass
    


