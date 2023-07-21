# get user inputs with validations
def choose_symbol():
    input_list = ['X', 'O']
    flag = False
    user_input = ''

    while not flag:
        user_input = input("Please select a symbol: ")

        if user_input.upper() in input_list:
            flag = True
        else:
            print("Wrong input. Expected inputs should be 'X' or 'O'.")

    return user_input.upper()


def user_inputs():
    input_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    flag = False
    user_input = ''
    error_msg = "Wrong input. Expected inputs should be numbers between 1-9."

    while not flag:
        user_input = input("Please choose a position between 1-9: ")

        if user_input in input_list:
            if user_input.isnumeric():
                flag = True
            else:
                print(error_msg)
        else:
            print(error_msg)

    return int(user_input)


# Create the board
def display_board(dic):
    print(dic.get(7) + '|' + dic.get(8) + '|' + dic.get(9))
    print(dic.get(4) + '|' + dic.get(5) + '|' + dic.get(6))
    print(dic.get(1) + '|' + dic.get(2) + '|' + dic.get(3))


# Replace the selected symbol to the selected position
def place_symbols_on_board(my_dic, value, symbol):
    if my_dic.get(value).strip() == '-'.strip():
        my_dic[value] = symbol
        display_board(my_dic)
    else:
        print('This position is already selected. Please choose any available positions.')

    return my_dic


# Possible wins
def possible_wins(user_list):
    win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for lst in win_list:
        if sorted(set(user_list).intersection(lst)) == lst:
            return True

    return False


# Execute the game
def execute_game():
    my_dic = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-'}
    win_list_x = []
    win_list_o = []

    input_symbol = choose_symbol()

    cnt = len(my_dic)
    change_symbol = False

    while cnt >= 1:
        if change_symbol:
            if input_symbol == 'X':
                input_symbol = 'O'
            elif input_symbol == 'O':
                input_symbol = 'X'

        print(f'Now playing {input_symbol}')
        input_value = user_inputs()

        if input_value not in win_list_x and input_value not in win_list_o:
            if input_symbol == 'X':
                win_list_x.append(input_value)
            elif input_symbol == 'O':
                win_list_o.append(input_value)
        else:
            print('This position is already selected. Please choose any available positions.')
            change_symbol = False
            continue

        place_symbols_on_board(my_dic, input_value, input_symbol)
        print('\n' * 2)

        if possible_wins(win_list_x):
            print("Congrats! 'X' wins the game")
            break
        if possible_wins(win_list_o):
            print("Congrats! 'O' wins the game")
            break

        cnt -= 1
        if cnt == 0:
            print("It's a tie game")

        change_symbol = True


execute_game()
