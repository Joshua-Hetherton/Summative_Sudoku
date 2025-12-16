# import time
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

    def __init__ (self, board:list[list[int]], size:int):
        """
        Initialises the Sudoku Game State, 
        containing frequently used variables that are throughout the code
        
        Args:
        list[list[int]] board: 2D list representing the Game Board
        int size: The Size of the Board (4, 9 or 16)

        """
        self.board = board #2d List of Sudoku Board
        self.size = size #Size of Grid(4, 9 or 16)
        self.box_size= int(size ** 0.5) # The Size of each box

    def __hash__(self) -> int:
        """
        Makes the state hashable so that it 
        can be used in sets and as dictionary keys, allowing greater flexibility

        Returns:
        int: Hash value of the board
        """
        
        return hash(str(self.board))
    
    def __eq__(self, other: object)-> bool:
        """
        Checks if the two sudoku boards are the same
        
        Args:
        Object other: Another Sudoku state object

        Returns:
        bool: Returns True if the boards are the same, otherwise False
        """

        return self.board == other.board
    
    def copy(self):
        """
        Creates a new copy of the state that is selected

        Returns:
        Sudoku_state: A new copy of the current state
        """
        return Sudoku_state([copy.deepcopy((self.board), self.size)])
        pass

    def valid_placement(self, row: int, col: int, num: int) -> bool:
        """
        Checks if the placement of num at row, col on the board is a valid move

        Args:
        int row: Description
        int col: Description
        int num: Description

        Returns:
        bool: if the placement isn't a valid move, False, otherwise returns True
        """

        if num in self.board[row]:
            return False
        if num in [self.board[r][col] for r in range(self.size)]:
            return False
        
        #Checking the boxes for valid placement
        box_row_start= row - row % self.box_size
        box_col_start= col - col % self.box_size

        for r in range(box_row_start, box_row_start + self.box_size):
            for c in range(box_col_start, box_col_start + self.box_size):
                if self.board[r][c]== num:
                    return False
                
        return True


    def find_empty_cell(self) -> tuple[int, int] | None:
        """
        Finds the first empty cell on the board
        Checks if it contains a 0, which represents if a cell is empty

        Returns:
        tuple[int, int] | None: Returns the row and column of the cell as a tuple, or returns None if No Empty cells are found
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col]==0:
                    return (row, col)
        
        return None

    def is_goal_state(self) -> bool:
        """
        Checks if this state is the same as the goal state (i.e if its solved) 
        All Cellls MUST be filled
        
        Returns:
        bool: It will retrun True if non empty cells are found, otherwise returns false, allowing the game to continue
        """

        return self.find_empty_cell() is None


    def get_successor(self) -> list["Sudoku_state"]:
        """
        Generate all the valid possible sucessor states

        Returns:
        list[Sudoku_state]: A list of all the valid successor states in the current state (i.e the possible numbers that can be placed)
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
        Displays the Sudoku Board, making it easily readable

        Returns:
        None
        """

        for i, row in enumerate(self.board):
            if i%self.box_size==0 and i>0:
                print("-"*(self.size*2 + self.box_size -1))
            str_row= ""
            for j, num in enumerate(row):
                if j%self.box_size==0 and j>0:
                    str_row += (str(num) if num !=0 else ".") + " "
            print(str_row)

def depth_first_search(initial_state: Sudoku_state):
    """
    Performs the DFS to solve the sudoku puzzle
    In this section, a visited set is used to keep track of all states explored, as to avoid the Multiple Parent states problem.
    DFS is implemented using a LIFO Stack.
    
    Args:
    Sudoku_state intital_state: Initial State of the Sudoku Puzzle

    Returns:
    tuple[Sudoku_state | None, int]: Returns the goal state if found, or returns None if no solution is found
    """

    #Checks if the is already in the goal state (i.e solved)
    if initial_state.is_goal_state():
        return initial_state ,1
    
    states_to_explore=[initial_state]

    visited= {initial_state}

    states_counter= 1
    try:
        while states_to_explore:

            state= states_to_explore.pop()

            successors= state.get_successor()

            for successor in successors:
                if successor.is_goal_state():
                    return successor, states_counter

                if successor not in visited:
                    visited.add(successor)
                    states_to_explore.append(successor)

            return None, states_counter
    except Exception as e:
        print(f"Error occured while performing DFS:\n{e}\n-------\nReturning Last Values found")
        return None, states_counter







    pass

def breath_first_search(initial_state: Sudoku_state):
    """
    Docstring for breath_first_search
    """
    if initial_state.is_goal_state():
        return initial_state ,1
    
    states_to_explore=[initial_state]
    visited={initial_state}

    states_counter=1
    try:
        while states_to_explore:
            state=states_to_explore.pop()
            sucessors= state.get_successor()

            for sucessor in sucessors:
                states_counter+=1
                if sucessor.is_goal_state():
                    return sucessor, states_counter
                
                if sucessor not in visited:
                    visited.add(sucessor)
                    states_to_explore.append(sucessor)
        return None, states_counter

    

    except Exception as e:
        print(f"Error occured while performing BFS:\n{e}\n-------\nReturning Last Values found")
        return None, states_counter
    pass

def get_run_results():
    """
    Docstring for get_run_results
    """
    pass

def main():
    """
    Docstring for main
    """
    print("Sudoku Solver using BFS:")
    print("-"*80)
    


if __name__ == "__main__":
    main()

