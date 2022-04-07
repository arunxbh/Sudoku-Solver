import requests
import json

level = input("Enter a difficulty (easy, medium, hard) to see solved: ")
#randomly generates a difficult level board
test_url = requests.get("https://sugoku.herokuapp.com/board?difficulty=" + level)
test_board = json.loads(test_url.text[9:190])

def print_board(board):
    # after every third row print a divider line
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        # length of row is retrieved from board[0]
        for j in range(len(board[0])):
            # makes sure a line is not printed on the left side from the first row
            # print a divider after each square of 3
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def solve(board):
    if not get_empty(board):
        return True
    else:
        row, col = get_empty(board)
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # check square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def get_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # return row and column of the empty location
                return (i, j)
    return False

def run(board, diff):
    print("Here is your randomly generated " + level + " board!")
    print("Unsolved:")
    print_board(board)
    solve(board)
    print(" ")
    reveal_solution = input("Hit 'enter' when you would like to see the solution")
    print(" ")
    print("Solved:")
    print_board(board)

run(test_board, level)

