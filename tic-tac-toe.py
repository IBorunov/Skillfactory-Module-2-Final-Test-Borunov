def playfield():
    print("      0   1   2  ")
    print("    -------------")
    for i in range(3):
        print(f"{i}   | {field[i][0]} | {field[i][1]} | {field [i][2]} |")
        print("    -------------")

def players_turn():
    while True:
        turn = input("Ваш ход: ").split()
        if len(turn) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = turn
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа!")
            continue

        x = int(x)
        y = int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Вводите числа от 0 до 2!")
            continue

        if field[x][y] != " ":
            print("Поле занято!")
            continue
        return x, y

def check_win():
    win_moves = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                     ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                     ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for move in win_moves:
        symbols = []
        for m in move:
            symbols.append(field[m[0]][m[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


field = [[" "] * 3 for i in range(3)]

for move in range(9):
    move += 1
    playfield()
    if move % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = players_turn()

    if move % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if move == 9:
        playfield()
        print(" Ничья!")

    if check_win():
        playfield()
        break