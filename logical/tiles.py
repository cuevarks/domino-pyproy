import random

# import logical.player ########

# logical.player.juan.player1 = [] #####
player1 = []
player2 = []
player3 = []
player4 = []

ficha = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2],
         [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]


# player_distribution
def player(item):
    if len(player1) <= 6:
        player1.append(item)
    elif len(player2) <= 6:
        player2.append(item)
    elif len(player3) <= 6:
        player3.append(item)
    else:
        player4.append(item)


# player1 = p.jugador.player1()

mano = [0, 0, 0, 0]
mesa = []
domino = ficha

g = 0
while len(domino) != 0:
    a = random.choice(domino)
    fd = domino.pop(domino.index(a))
    player(fd)
    print(fd)
print(player1, player2, player3, player4)
turno = 0

while len(player1) != 0 or len(player2) != 0 or len(player3) != 0 or len(player4) != 0:
    table = [player1, player2, player3, player4]
    print("Introdusca un valor")
    # a = input()
    for x in range(0, 3):
        if [6, 6] in table[x]:
            break
    if x % 2 == 0:
        mano[0] = table[x]
        if x == 0:
            mano[2] = table[2]
            mano[1] = table[1]
            mano[3] = table[3]
        else:
            mano[2] = table[0]
            mano[1] = table[1]
            mano[3] = table[3]
    else:
        mano[0] = table[x]
        if x == 1:
            mano[1] = table[0]
            mano[2] = table[3]
            mano[3] = table[2]
        else:
            mano[1] = table[0]
            mano[2] = table[1]
            mano[3] = table[2]

    print(mesa, '\n', table)
    break
    # turno +=1
    # if table[turno][a] == [6,6]:
    # print("fn")
while True:
    for il in range(0, 4):
        print("player", il + 1)
        for t in range(0, len(mano[il])):
            print((t + 1), ": ", mano[il][t])
        print(t + 2, ": Turno siguiente")
        re = input()
        print("Derecha (Der) o izquierda (iz)")
        deis = input()  # type: str
        if int(re) <= len(mano[il]):
            fch = mano[il].pop(mano[il].index(mano[il][int(re) - 1]))
            if len(mesa) == 0:
                mesa.append(fch)
            elif mesa[len(mesa) - 1][1] == fch[1] and str(deis) == "Der":
                fch[0], fch[1] = fch[1], fch[0]
                mesa.append(fch)
            elif mesa[len(mesa) - 1][1] == fch[0] and str(deis) == "Der":
                mesa.append(fch)
            elif mesa[0][0] == fch[0] and str(deis) == "iz":
                fch[0], fch[1] = fch[1], fch[0]
                mesa.insert(0, fch)
            elif mesa[0][0] == fch[1] and str(deis) == "iz":
                mesa.insert(0, fch)
        print(mesa)
        if len(mano[0]) == 0 or len(mano[1]) == 0 or len(mano[2]) == 0 or len(mano[3]) == 0:
            break
