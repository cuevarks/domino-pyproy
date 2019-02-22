import random
import logical.player ########

logical.player.juan.player1 = [] #####
player1 = []
player2 = []
player3 = []
player4 = []

ficha = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2],
         [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]


def player_distribution(item):
    if len(player1) <= 6:
        player1.append(item)
    elif len(player2) <= 6:
        player2.append(item)
    elif len(player3) <= 6:
        player3.append(item)
    else:
        player4.append(item)


# player1 = p.jugador.player1()

mesa = [0, 0, 0, 0]
domino = ficha
g = 0
while len(domino) != 0:
    a = random.choice(domino)
    fd = domino.pop(domino.index(a))
    logical.player(fd) ###########
    print(fd)
print(player1, player2, player3, player4)
turno = 0

while True:
    # len(player1) != 0 or len(player2) != 0 or len(player3) != 0 or len(player4) != 0:
    table = [player1, player2, player3, player4]
    print("Introduzca un valor")
    # a = input()
    for x in range(0, 3):
        if [6, 6] in table[x]:
            break
    if x % 2 == 0:
        mesa[0] = table[x]
        if x == 0:
            mesa[2] = table[2]
            mesa[1] = table[1]
            mesa[3] = table[3]
        else:
            mesa[2] = table[0]
            mesa[1] = table[1]
            mesa[3] = table[3]
    else:
        mesa[0] = table[x]
        if x == 1:
            mesa[1] = table[0]
            mesa[2] = table[3]
            mesa[3] = table[2]
        else:
            mesa[2] = table[1]
            mesa[1] = table[0]
            mesa[3] = table[2]

    print(mesa, '\n', table)

    break

    # turno +=1
    # if table[turno][a] == [6,6]:
    # print("fn")









