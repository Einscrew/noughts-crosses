def print_m(m):
    print("-"*7)
    for i in range(3):
        line = "|"
        for j in range(3):
            line += m[i][j]+"|"
        print(line)
        print("-" * 7)


def update_m(m, l, char):
        for i in range(2):
            if l[i] > 2 and l[i] < 0:
                return -1
        if m[l[0]][l[1]] != " ":
            return -1
        else:
            m[l[0]][l[1]] = char


def check_victory(m):
    for i in range(2):
        if m[i][0] == m[i][1] and m[i][1] == m[i][2]:
            return m[i][1]
        if m[0][i] == m[1][i] and m[1][i] == m[2][i]:
            return m[1][i]

    if m[0][0] == m[1][1] and m[1][1] == m[2][2]:
        return m[1][1]

    if m[2][0] == m[1][1] and m[1][1] == m[0][2]:
        return m[1][1]

    return " "


def main_cycle():
    m = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    p1 = "Player 1"
    p2 = "Player 2"
    p1symbol = "X"
    p2symbol = "O"

    i = 0

    while i >= 0:
        if i % 2 == 0:
            player = p1
            symbol = p1symbol
        else:
            player = p2
            symbol = p2symbol

        lst = [int(x)-1 for x in input(player + " - Please input the line and the column.").split()]
        while update_m(m, lst, symbol) == -1:
            lst = [int(x)-1 for x in input(player + " - Please insert a correct pair os values.").split()]
        print_m(m)
        win = check_victory(m)
        if win == p1symbol:
            winner = p1
            break
        elif win == p2symbol:
            winner = p2
            break
        i += 1

    print("The winner is: " + winner)


main_cycle()
