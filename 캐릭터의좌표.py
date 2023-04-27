keyinput1 = ["left", "right", "up", "right", "right"]
board1 = [11, 11]
keyinput2 = ["down", "down", "down", "down", "down"]
board2 = [7, 9]


def solution(keyinput, board):
    xlim, ylim = board[0]//2, board[1]//2
    move = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    x, y = 0, 0

    for i in keyinput:
        in_x, in_y = move[i]
        if abs(x+in_x) > xlim or abs(y+in_y) > ylim:
            continue
        else:
            x, y = x+in_x, y+in_y
    return [x, y]


result1 = solution(keyinput1, board1)
print(result1)
result2 = solution(keyinput2, board2)
print(result2)
