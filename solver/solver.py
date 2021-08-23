board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0], 
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def solve(bo):     #finding num to try (recursively)

    find = find_empty(bo)
    if not find:
        return True       #the solution is completed 
    else:
        row, col = find   #returning position to put number

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i     #adding the value to board if its valid

            if solve(bo):       #recursive call
                return True

            bo[row][col] = 0      #backtracking to last position if the solution is not valid

    return False


def valid(bo, num, pos):     #checking if the current board is valid by checking if the number put by algo is not already present on the board
                             #bo is the input board,num is the number put by algo,pos is the current position i.e. the value returned by find_empty() function.
    
    for i in range(len(bo[0])):    #checking each row 
        if bo[pos[0]][i] == num and pos[1] != i:   
            return False


    for i in range(len(bo)):       #checking each column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    
    box_x = pos[1] // 3     #checking in which 3x3 square the head currently is
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):      #checking each 3x3 square
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):        #printing a visual representation of the sudoku board  
                  
    for i in range(len(bo)):      #printing -- and | symbol to separate 9x9 board into 9 smaller 3x3 boards  
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")       
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")      


            if j == 8:               #doing the "\n" fucntion to go to the next line if the head is at the last position of the row
                print(bo[i][j])        
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):      #finding and returning empty space on the board to try and put number in   
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)      #returning the tuple (row,column) [unlike usual terms where it returns column,row]

    return None

print_board(board)
solve(board)
print("___________________")
print_board(board)
