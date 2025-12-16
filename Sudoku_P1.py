import time
import copy
from collections import deque
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
        return Sudoku_state(copy.deepcopy(self.board), self.size)

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
                states_counter+=1
                if successor.is_goal_state():
                    return successor, states_counter

                if successor not in visited:
                    visited.add(successor)
                    states_to_explore.append(successor)
        return None, states_counter
        
    except Exception as e:
        print(f"Error occured while performing DFS:\n{e}\n-------\nReturning Last Values found")
        return None, states_counter


def breadth_first_search(initial_state: Sudoku_state):
    """
    Performs the DFS to solve the sudoku puzzle
    In this section, a visited set is used to keep track of all states explored, as to avoid the Multiple Parent states problem.
    DFS is implemented using a FIFO Queue (this is done by using popleft() from the collections.deque module, built into python)
    
    Args:
    Sudoku_state intital_state: Initial State of the Sudoku Puzzle

    Returns:
    tuple[Sudoku_state | None, int]: Returns the goal state if found, or returns None if no solution is found
    """
    if initial_state.is_goal_state():
        return initial_state ,1
    
    states_to_explore=deque([initial_state])
    visited={initial_state}

    states_counter=1
    try:
        while states_to_explore:
            state=states_to_explore.popleft()
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

def get_run_results(board: list[list[int]], size: int, difficulty: str, algorithm_name: str)-> tuple[int,float]:
    """
    Runs a single search and reports the results
    """
    initial_state= Sudoku_state(board, size)
    print("\n Initial Board:")
    initial_state.display()

    start_time= time.time()

    if algorithm_name=="BFS":
        solution_state, states_explored= breadth_first_search(initial_state)

    elif algorithm_name=="DFS":
        solution_state, states_explored= depth_first_search(initial_state)

    else:
        raise ValueError("Invalid Algorithm Name, Use BFS or DFS")
    
    end_time= time.time()
    running_time=end_time - start_time

    if solution_state:
        print(f"""\n Solution Has Been Found!
            States explored: {states_explored}
            Time taken: {running_time:.3f} seconds
            Solution Board:""")
        
        solution_state.display()

    else:
        print(f"""No Solution Found
                States explored: {states_explored}
                Time taken: {running_time:.3f} seconds
              """)
        
    return states_explored, running_time

def board_sizes(difficulty: str, board_size: int)-> list[list[int]]:
    """
    Determines the 2D list board that is to be used based off the users input of difficults and board size

    Args:
    str difficulty: Description
    int board_size: Description

    Returns:
    list[list[int]]: The 2D list representing the board
    """
    match difficulty, board_size:
        case "Easy", 4:
            return [[4, 2, 0, 0],
                    [0, 0, 0, 0],
                    [0, 3, 4 ,0],
                    [0, 0, 1, 0]
                    ]
        case "Medium", 4:
            return [[3, 0, 1, 0],
                    [2, 0, 0, 0],
                    [0, 0, 0, 1],
                    [0, 2, 4, 0]]
        case "Hard", 4:
            return [[3, 4, 0, 0], 
                    [0, 0, 4, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1]]
        case "Very Hard", 4:
            return [[3, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 4, 0, 3],
                    [0, 0, 0, 1]]

        case "Easy", 6:
            return [[5, 3, 0, 4, 0, 6],
                    [4, 6, 0, 5, 3, 1],
                    [1, 2, 4, 0, 5, 3],
                    [6, 0, 3, 0, 0, 2], 
                    [3, 4, 0, 2, 1, 5],
                    [0, 1, 5, 3, 0, 4]]
        case "Medium", 6:
            return [[0, 0, 2, 1, 0, 0],
                    [0, 5, 6, 0, 4, 0],
                    [5, 0, 4, 3, 1, 6],
                    [6, 0, 3, 0, 2, 0],
                    [0, 4, 0, 6, 5, 2],
                    [2, 0, 0, 4, 0, 0]]
        case "Hard", 6:
            return [[0, 0, 0, 0, 0, 5],
                    [2, 3, 5, 0, 4, 0],
                    [0, 0, 0, 4, 2, 6],
                    [0, 4, 2, 0, 3, 0],
                    [3, 0, 1, 5, 0, 0],
                    [0, 0, 6, 0, 1, 0]]
        case "Very Hard", 6:
            return [[0, 3, 0, 0, 1, 6],
                    [6, 0, 1, 0, 0, 0],
                    [0, 5, 2, 0, 0, 0],
                    [0, 0, 0, 0, 5, 3],
                    [0, 0, 0, 0, 6, 0],
                    [0, 0, 6, 0, 0, 4]]

        case "Easy", 9:
            return [[6, 0, 4, 5, 0, 0, 3, 9, 8],
                    [9, 0, 0, 6, 0, 0, 0, 7, 4],
                    [0, 0, 8, 0, 0, 0, 6, 2, 1],
                    [0, 0, 0, 0, 0, 0, 1, 0, 6],
                    [0, 1, 0, 4, 0, 3, 9, 5, 7],
                    [0, 8, 9, 0, 0, 6, 2, 4, 3],
                    [7, 0, 3, 0, 5, 0, 4, 1, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 2],
                    [1, 4, 0, 0, 0, 9, 8, 0, 0]]
        case "Medium", 9:
            return [[9, 0, 0, 0, 0, 0, 0, 0, 0],
                    [6, 0, 0, 0, 1, 7, 3, 4, 2],
                    [0, 0, 0, 8, 3, 0, 0, 0, 6],
                    [0, 0, 4, 6, 0, 3, 1, 0, 0],
                    [0, 0, 0, 0, 0, 2, 5, 0, 0],
                    [3, 2, 0, 0, 0, 5, 4, 6, 7],
                    [0, 0, 0, 0, 0, 0, 0, 0, 4],
                    [7, 6, 0, 0, 0, 0, 2, 1, 5],
                    [0, 0, 0, 0, 0, 0, 6, 0, 9]]
        case "Hard", 9:
            return [[4, 0, 0, 0, 7, 0, 0, 0, 0],
                    [0, 0, 7, 0, 9, 0, 4, 0, 1],
                    [0, 1, 0, 0, 6, 0, 0, 0, 0],
                    [5, 4, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 8, 0, 0, 0, 5, 0, 2],
                    [9, 2, 0, 0, 0, 5, 0, 8, 4],
                    [0, 0, 0, 3, 0, 6, 0, 1, 0],
                    [3, 0, 0, 0, 0, 8, 0, 0, 0],
                    [0, 5, 0, 0, 2, 4, 0, 0, 7]]
        case "Very Hard", 9:
            return [[0, 0, 2, 0, 0, 0, 0, 0, 9],
                    [7, 0, 0, 4, 0, 0, 0, 0, 0],
                    [0, 0, 9, 0, 6, 0, 0, 3, 0],
                    [2, 0, 0, 7, 8, 4, 0, 0, 0],
                    [6, 0, 0, 1, 0, 0, 0, 0, 7],
                    [0, 0, 4, 2, 0, 0, 0, 0, 0],
                    [0, 0, 3, 0, 2, 0, 8, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 5, 0],
                    [1, 0, 0, 9, 0, 3, 4, 0, 0]]
        

def main():
    """
    Docstring for main
    """
    print("Sudoku Solver using BFS:")
    print("-"*80)
    
    


if __name__ == "__main__":
    main()

