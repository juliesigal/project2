import random

board = [['_','_','_'],['_','_','_'],['_','_','_']]
current_b = ''
for i in board:
    for j in i:
        current_b += '_'

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
b = '_o______o'
b2 = '_________'
spot = 3
sign = 'x'
current_b= convert_xo(b,spot,sign)
print(present_board(current_b))
