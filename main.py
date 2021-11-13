import random

board = [['_','_','_'],['_','_','_'],['_','_','_']]
current_b = ''
for i in board:
    for j in i:
        current_b += '_'

def present_board(b):
    return f'{b[0:3]}  \n{b[3:6]}  \n{b[6:9]}'

def convert_xo(b,b2,spot,sign):
    x = b.split()
    y = b2.split()
    for i in range(len(b)):
        print(i)
        if i != spot:
            continue
        else:
            if b[i] == '_':
                b2[i] == sign

    return b2
b = '_________'
b2 = '_________'
spot = 3
sign = 'x'
#print(convert_xo(b,b2,spot,sign))
print(present_board(board))
