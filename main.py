board = list(range(1,10))
def print_board(board):
    print("_" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def check_win(board):
    win_combs = ((0,1,2), (0,4,8), (2,4,6), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8))
    for i in win_combs:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def player_turn(token):
    valid = False
    check_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    while not valid:
        answer = int(input("Ваш ход " + token + ": "))
        if answer not in check_list:
            print("Некорректный ввод!")
        else:
            if (str(board[answer - 1]) not in "XO"):
                board[answer - 1] = token
                valid = True
            else:
                print("Клетка занята !")

def main(board):
    counter = 0
    win = False
    while not win:
        print_board(board)
        if counter % 2 == 0:
            player_turn("X")
        else:
            player_turn("O")
        counter += 1
        if counter > 4:
            temp = check_win(board)
            if temp:
                print(f"Игрок {temp} победил!")
                win = True
                break
        if counter == 9:
            print("Ничья")
            break
    print_board(board)


main(board)