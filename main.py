def present_board(b):      #present the board in 3 different lines to the user
    return f'{b[0:3]}  \n{b[3:6]}  \n{b[6:9]}'

def get_user_sign(b):    #get user's choice, check if it's an integer, if it's legal and free
    while True:
        s = input('please enter number of field')
        if s.isdigit():    #check if it's an integer
            s = int(s)
            if s < 0 or s > 9:      #if it's legal
                print('this spot is not exist')
                continue
            else:
                for i in list(b):    # if it's free
                    if b[s] == '_':
                        return s
                    else:
                        print("it's occupied, try again")
                        break

def convert_xo(b,spot,s):    #replace user's choice in the string
    y = []
    for i in range(len(b)):
        if i == spot:
            y.append(sign)
        else:
            y.append(b[i])
    return ''.join(y)

def check_win(b,s):    #check all the 8 ways to win
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
print('welcome to the tic-tac-toe game. first player get plays with x and second plays with o. good luck.')
print(present_board(board))

for i in range(len(board)):    #run on all string fields
    player_choice = get_user_sign(board)     #check if player 1(x) or 2(o)
    if i % 2 == 0:
        sign = 'x'
    else:
        sign = 'o'
    current_b = convert_xo(board, player_choice, sign)
    board = current_b
    print(present_board(board))
    if check_win(board,sign):                 #check if it's win before the end of the game
        print(check_win(board,sign))
        break
        if i == 8:
            print("it's a draw")         
