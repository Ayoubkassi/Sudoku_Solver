board = [
[4,0,6,5,0,2,8,0,9],
[0,0,0,0,4,0,0,3,0],
[0,0,0,0,0,0,0,0,5],
[6,0,0,8,0,0,1,0,0],
[5,0,0,0,7,0,0,8,0],
[3,0,2,9,0,4,0,6,0],
[0,2,0,6,0,0,0,0,1],
[0,0,0,0,5,3,9,4,0],
[8,3,0,0,9,0,0,0,2]
]

# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

#
# def solve(bo):
#     find = find_empty(bo)
#     if not find:
#         return True
#     else:
#         row, col = find
#
#     for i in range(1,10):
#         if valid(bo, i, (row, col)):
#             bo[row][col] = i
#
#             if solve(bo):
#                 return True
#
#             bo[row][col] = 0
#
#     return False

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row , col = find
        for i in range (1,10):
            if(valid(board,i,(row,col))):
                board[row][col] = i

                if solve(board):
                    return True

                #back track reset the element
                board[row][col] = 0

        return False




def valid(board,num,pos):
    #check row
    size = len(board[0])
    for i in range (size):
        if(board[pos[0]][i] == num and pos[1] != 0):
            return False

    #check col
    for j in range (size):
        if(board[j][pos[1]] == num and pos[0] != j):
            return False

    #check group

    #code the logic to see if is it valid in box
    #get box number we have 9

    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range (3):
        for j in range(3):
            if(board[box_x*3+i][box_y*3+j] == num and (box_x*3+i,box_y*3+j)!= pos):
                return False


    return True


# def valid(bo, num, pos):
#     # Check row
#     for i in range(len(bo[0])):
#         if bo[pos[0]][i] == num and pos[1] != i:
#             return False
#
#     # Check column
#     for i in range(len(bo)):
#         if bo[i][pos[1]] == num and pos[0] != i:
#             return False
#
#     # Check box
#     box_x = pos[1] // 3
#     box_y = pos[0] // 3
#
#     for i in range(box_y*3, box_y*3 + 3):
#         for j in range(box_x * 3, box_x*3 + 3):
#             if bo[i][j] == num and (i,j) != pos:
#                 return False
#
#     return True



#printing the board
def printBoard(arr):
    size = len(arr[0])
    for i in range (size):
        if(i%3 == 0 and i!= 0):
            print("--------------------")
        for j in range (size):
            if(j == 3 or j == 6):
                print("|",end="")
            print(arr[i][j],end=" ")
        print("")




def findEmpty(arr):
    size = len(arr[0])
    for i in range (size):
        for j in range (size):
            if(arr[i][j] == 0):
                return (i,j)

    return None

# def find_empty(bo):
#     for i in range(len(bo)):
#         for j in range(len(bo[0])):
#             if bo[i][j] == 0:
#                 return (i, j)  # row, col
#
#     return None



printBoard(board)
solve(board)

print("\n\nSolution is : \n\n")
printBoard(board)
