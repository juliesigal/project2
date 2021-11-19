import random

def present_board(b):
    return f'{b[0:3]}  \n{b[3:6]}  \n{b[6:9]}'

def convert_xo(b,spot,sign):
    y = []
    for i in range(len(b)):
        if i == spot:
            y.append(sign)
        else:
            y.append(b[i])
    return ''.join(y)

def get_user_sign(b):
    for i in range(len(b)):
        s = int(input('please pick a spot in a field'))
        y = len(b)
        if s < 0 or s >= y:
            print('this spot is not exist')
            continue
        elif s == i:
            if b[i] != '_':
                print('occuped')
                continue
    return s

def check_win(b,sign):
    for i in list(b):
        if b[0] == sign and b[1] == sign and b[2] == sign\
            or b[3] == sign and b[4] == sign and b[5] == sign\
            or b[6] == sign and b[7] == sign and b[8] == sign\
            or b[0] == sign and b[3] == sign and b[6] == sign\
            or b[1] == sign and b[4] == sign and b[7] == sign\
            or b[2] == sign and b[5] == sign and b[8] == sign\
            or b[0] == sign and b[4] == sign and b[8] == sign\
            or b[2] == sign and b[4] == sign and b[6] == sign:
            return f'player {sign} won'



board = '_________'

for i in range(len(board)):
    x = get_user_sign(board)
    current_b = convert_xo(board, x, 'x')
    board = current_b
    print(present_board(board))
    y = get_user_sign(board)
    current_b = convert_xo(board, y, 'o')
    board = current_b
    #print(check_win(board, 'y'))
    print(present_board(board))

