def feild_print():
    print(f"{game[0]}|{game[1]}|{game[2]}")
    print(f"{game[3]}|{game[4]}|{game[5]}")
    print(f"{game[6]}|{game[7]}|{game[8]}")

# сама игра
def play_game():
    global game, current_player
    game = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"
    moves = 0
    feild_print()

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    while True:
        # проверка хода
        while True:
            move = input(f"\nИгрок {current_player}, введите число: ")
            if not move.isdigit():
                print("Введите число!")
                continue
            choice = int(move)
            if choice < 1 or choice > 9:
                print("Только числа от 1 до 9!")
                continue
            if game[choice - 1] in ["X", "O"]:
                print("Клетка занята!")
                continue
            break

        game[choice - 1] = current_player
        moves += 1
        feild_print()

        # проверка победы
        for combo in winning_combinations:
            if game[combo[0]] == game[combo[1]] == game[combo[2]]:
                print(f"\nПобедил {current_player}!")
                return

        # проверка ничьи
        if moves == 9:
            print("\nКлетки закончились, НИЧЬЯ!")
            return

        # смена игрока
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# САМА ИГРА
print("Добро пожаловать в игру Крестики и Нолики!")

while True:
    play_game()
    answer = input ("\nХотите сыграть еще? (ДА/НЕТ): ")
    if answer.lower() != "да":
        print(" Спасибо за игру! ")
        exit()
    else:
        continue