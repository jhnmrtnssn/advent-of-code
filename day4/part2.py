# Advent of Code - Day 4
# Part 2

def loadNumbersAndBoards():
    all_bingo_boards = list([])
    bingo_board = list([])
    id = 0

    # Store all bingo boards from input file
    for index, line in enumerate(open("input.txt")):
        if index == 0:
            bingo_numbers = list(map(int, line.strip().split(",")))

        if index > 1:
            if line.strip() == "":
                all_bingo_boards.append(bingo_board)
                bingo_board = []
                id += 1
            else:
                row = line.strip().split(" ")
                while len(row) > 5:
                    row.remove("")
                bingo_board.append(list(map(int, row)))

    return bingo_numbers, all_bingo_boards


def isNumberInBoard(board, number):
    for row in board:
        for num in row:
            if num == number:
                return True
    return False


def markBingoBoard(board, number):
    for row_id, row in enumerate(board):
        for col_id, num in enumerate(row):
            if num == number:
                board[row_id][col_id] += 1000


def hasBingo(board):
    # Check for all rows
    for row in board:
        if sum(row) > 5000:
            return True

    # Check for all columns
    for col_id in range(5):
        col = []
        for row in range(5):
            col.append(board[row][col_id])
        if sum(col) > 5000:
            return True
    return False


###### Part 2 ######

bingo_numbers, all_bingo_boards = loadNumbersAndBoards()

playing = True
for number in bingo_numbers:
    boards_with_bingo = 0
    for board in all_bingo_boards:
        if isNumberInBoard(board, number):
            markBingoBoard(board, number)
        if hasBingo(board):
            boards_with_bingo += 1

    # Replay with last bingo board that did not win
    if boards_with_bingo == 98:
        for board in all_bingo_boards:
            if not hasBingo(board):
                for replay_number in bingo_numbers:
                    if isNumberInBoard(board, replay_number):
                        markBingoBoard(board, replay_number)
                    if hasBingo(board):
                        losing_board = board
                        last_number = replay_number
                        playing = False
                        break

    if playing == False:
        break

unmarked_sum = 0
for row in losing_board:
    for num in row:
        if num < 1000:
            unmarked_sum += num

print(unmarked_sum*last_number)
