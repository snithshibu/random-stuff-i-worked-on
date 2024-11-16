"""
    sample board:
    5 3 0 0 7 0 0 0 0
    6 0 0 1 9 5 0 0 0
    0 9 8 0 0 0 0 6 0
    8 0 0 0 6 0 0 0 3
    4 0 0 8 0 3 0 0 1
    7 0 0 0 2 0 0 0 6
    0 6 0 0 0 0 2 8 0
    0 0 0 4 1 9 0 0 5
    0 0 0 0 8 0 0 7 9
"""

#function for user to input the values to the grid
def get_board(size): 
    print(f"Please enter the matrix values row by row, with {size} values per row, separated by spaces.")
    
    b = [] #the grid that will be inputted by the user
    for i in range(size):
        while True:
            row = input(f"Enter row {i+1}: ").strip() #this is a list
            row_values = row.split() #list with row values is now seperated
            if len(row_values) != size: #in case of human error
                print(f"Error: You must enter exactly {size} values for row {i+1}. Try again.")
                continue
            
            try:
                row_values = [int(value) for value in row_values]
                if any(v < 0 or v > 9 for v in row_values): #ensures all values are in the range
                    print("Error: All values must be between 0 and 9. Try again.")
                    continue
                b.append(row_values) #appended to our grid
                break
            
            except ValueError: #ensures all values are integers
                print("Error: All values must be integers. Try again.")
    
    return b

#function to print the board that we have inputted, while also formatting it to look like a grid.
def print_board(b):
    for i in range(len(b)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - -") #for horizontal division
        
        for j in range(len(b[0])):
            if j%3==0 and j!=0:
                print(" | ", end="") #for vertical division
            
            if j == 8: 
                print(b[i][j]) #to go to the next line
            else:
                print(str(b[i][j]) + " ", end="")

#function to find the empty spaces in the grid. In this case, that would be zero.
def find_empty_space(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==0:
                return (i, j) #return row and column

    return None

#function to check if the board is valid i.e. the numbers we have added actually belong in that space
def valid(b, num, pos): #b for board, num for number, pos for position
    
    #to check row
    for i in range(len(b[0])): 
        if b[pos[0]][i]==num and pos[1]!=i: #checks if we added a number to that position prior and ignore it
            return False
    
    #to check column
    for i in range(len(b)): 
        if b[i][pos[1]]==num and pos[0]!=i: #checks if we added a number to that position prior and ignore it
            return False
    
    #to check which of the 9 boxes we are currently in
    ba=pos[1]//3
    bb=pos[0]//3

    for i in range(bb*3, bb*3 +3):
        for j in range(ba*3, ba*3 +3):
            if b[i][j]==num and (i,j)!=pos:
                return False

    return True

#function which solves the sudoku, it is recursive
def solve(b):
    find = find_empty_space(b) #calling our function above
    if not find:
        return True
    else:
        row, col =find

    for i in range(1,10):
        if valid(b, i, (row, col)):
            b[row][col]=i #adding it to the grid
            
            if solve(b): #recursive call
                return True
            
            b[row][col]=0 #backtracking if solve function is not true
    
    return False   

print("Welcome to the Sudoku Solver")
size = int(input('Enter the size of the sudoku grid: '))  # Size of the Sudoku matrix is inputted
print(f"Please input a {size}x{size} matrix.")   
board = get_board(size)
    
print("\nYour entered sudoku grid is:")
print_board(board)

print("\nSolving your sudoku puzzle....")

print("\nYour solved puzzle is:")
solve(board)
print_board(board)
