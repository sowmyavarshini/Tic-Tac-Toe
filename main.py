position = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
board = f'{position[0]} | {position[1]} | {position[2]}\n' \
        f'-----------\n' \
        f'{position[3]} | {position[4]} | {position[5]}\n' \
        f'-----------\n' \
        f'{position[6]} | {position[7]} | {position[8]}'


def compare(p, player1, player2):
    if p[0] == p[1] == p[2] == player1 or p[3] == p[4] == p[5] == player1 or p[6] == p[7] == p[8] == player1 or \
            p[0] == p[3] == p[6] == player1 or p[1] == p[4] == p[7] == player1 or p[2] == p[5] == p[8] == player1 or\
            p[0] == p[4] == p[8] == player1 or p[2] == p[4] == p[6] == player1:
        print('Player 1 win')
        return True
    elif p[0] == p[1] == p[2] == player2 or p[3] == p[4] == p[5] == player2 or p[6] == p[7] == p[8] == player2 or\
            p[0] == p[3] == p[6] == player2 or p[1] == p[4] == p[7] == player2 or p[2] == p[5] == p[8] == player2 or\
            p[0] == p[4] == p[8] == player2 or p[2] == p[4] == p[6] == player2:
        print('Player 2 win')
        return True
    else:
        return False


def update_board(p):
    new_board = f'{p[0]} | {p[1]} | {p[2]}\n' \
            f'-----------\n' \
            f'{p[3]} | {p[4]} | {p[5]}\n' \
            f'-----------\n' \
            f'{p[6]} | {p[7]} | {p[8]}'
    print(new_board)


def play_game():
    player1 = input("Player 1: Choose X or O :")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print('Start the game')
    print(board)
    game = True
    i = 1
    while game and i <= 5:
        p1_choice = input('Player1:Choose a position(1-9) available on the table: ')
        if p1_choice in position:
            position[int(p1_choice) - 1] = player1
            update_board(position)
        else:
            print('Choose another available position')
        if compare(position, player1, player2):
            break
        if i == 5:
            print('Game Draw')
            break
        p2_choice = input('Player2:Choose a position(1-9) available on the table: ')
        if p2_choice in position:
            position[int(p2_choice) - 1] = player2
            update_board(position)
        else:
            print('Choose another available position')
        if compare(position, player1, player2):
            game = False
        i += 1


play_game()
