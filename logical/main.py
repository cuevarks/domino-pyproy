# -*- coding: utf-8 -*-

from logical.player import Player
from logical.turn import Turn
import logical.turn
from logical.game_logic import Game
#from logical2.score import
from logical.tiles import Tiles
constraint, names, myPlayers, myTurns, turnList = True, [], [], [], []
Domino = Tiles.ficha


def constraints(input_value):
    if isinstance(input_value, int):
        return False
    return None

def presentar(mes):
    s = []
    for g in range(0, len(mes)):
        t = str('[{}|{}]'.format(mes[g][0], mes[g][1]))
        s.append(t)
    return s

def switch(fch, mesa, deis):
    if (mesa[len(mesa) - 1][1] == fch[1]) and (str(deis) == "D" or str(deis) == "d"):
        fch[0], fch[1] = fch[1], fch[0]
        return fch
    elif (mesa[len(mesa) - 1][1] == fch[0]) and (str(deis) == "D" or str(deis) == "d"):
        return fch
    elif (mesa[0][0] == fch[0]) and (str(deis) == "I" or str(deis) == "i"):
        fch[0], fch[1] = fch[1], fch[0]
        return fch
    elif (mesa[0][0] == fch[1]) and (str(deis) == "I" or str(deis) == "i"):
        return fch

def ifmi(a):
    if a == 2:
        return 14
    else:
        return 7
print("--------- DOMINÓ ER CIBAO v1.1 ---------")


while constraint:

    aux = input("¿Cuántos van a jugar? \n")
    if constraints(aux):
        print("\n Introduzca un numero")
        break
    aux = int(aux)
    if aux != 2 and aux != 4:
        print("\nNúmero inválido")
    else:
        amount = aux
        constraint = False

for player_number in range(0, amount):
    mano = []
    name = input("Nombre jugador " + str(player_number + 1) + ":\n")
    myTiles = Tiles()
    for inp in range(0, ifmi(amount)):
        a, Domino = Tiles.randomiz(Domino)
        mano.append(a)
    myPlayers.append(Player(name, mano, 0, 7))


#
#myTurns = Turn(myPlayers)
#turnList = myTurns.get_turn()
# #
#myTurns = Turn(myPlayers)

#Turn.check_double(myPlayers)

'''
for f in range(0, Tiles.ifmi(amount)):
    print(myPlayers[f].player_tiles)
'''
juego = True

myPlayers = Turn.switch(myPlayers)

mesa = []

while juego:
    for il in range(0, amount):
        passs1 = False
        passs = True
        while passs:
            print(myPlayers[il].player_name)
            for y in range(0, len(myPlayers[il].player_tiles)):
                print(y+1, ": ", '[{}|{}]'.format(myPlayers[il].player_tiles[y][0],myPlayers[il].player_tiles[y][1]))
            print(y + 2, ": Turno siguiente", "\n")
            re = int(input())
            #print(len(myPlayers[il].player_tiles), re)
            if re > len(myPlayers[il].player_tiles) :
                passs = False
                passs1 = True
                break
            elif Game.check(mesa, myPlayers[il].player_tiles[re - 1]):
                passs = False
                break
            else:
                print("Esa ficha no combina con las otras")
                g = presentar(mesa)
                print(''.join(g))
        if passs1:
            print("Turno siguiente")
        elif len(mesa) == 0 and re <= y + 1:
            fch = myPlayers[il].player_tiles.pop(re - 1)
            mesa.append(fch)
        elif Game.check2(mesa, myPlayers[il].player_tiles[re - 1]) == "i":
            print(Game.check2(mesa, myPlayers[il].player_tiles[re - 1]))
            fch = myPlayers[il].player_tiles.pop(re - 1)
            mesa.insert(0, switch(fch, mesa, "i"))
        elif Game.check2(mesa, myPlayers[il].player_tiles[re - 1]) == "d":
            fch = myPlayers[il].player_tiles.pop(re - 1)
            mesa.append(switch(fch, mesa, "d"))
        elif Game.check2(mesa, myPlayers[il].player_tiles[re - 1]) == "di":

            fch = myPlayers[il].player_tiles.pop(re - 1)
            k = True
            while k:
                print("Derecha (D) o izquierda (i)")
                deis = input()
                if deis == "I" or deis == "i":
                    mesa.insert(0, switch(fch, mesa, deis))
                    k = False
                elif deis == "D" or deis == "d":
                    mesa.append(switch(fch, mesa, deis))
                    k = False
                else:
                    k = True
        g = presentar(mesa)
        print(''.join(g))
        if len(myPlayers) == 4:
            if len(myPlayers[0].player_tiles) == 0 or len(myPlayers[1].player_tiles) == 0 or len(myPlayers[2].player_tiles) == 0 or len(myPlayers[3].player_tiles) == 0:
                juego = Game.ganarcheck(myPlayers)

                break
        else:
            if len(myPlayers[0].player_tiles) == 0 or len(myPlayers[1].player_tiles) == 0:
                juego = Game.ganarcheck(myPlayers)
                break
            #myPlayers[il].player_tiles[re - 1].index(myPlayers[il].player_tiles[re - 1]))


#for playtiles in range(0, len(myPlayers)):
    #print(myPlayers[playtiles].player_tiles)

###