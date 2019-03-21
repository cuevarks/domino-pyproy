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
    for inp in range(0, Tiles.ifmi(amount)):
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

sw = Turn.check_double(myPlayers)
myPlayers[sw], myPlayers[0] = myPlayers[0], myPlayers[sw]

mesa = []

while juego:
    for il in range(0, amount):
        passs = True
        while passs:
            print(myPlayers[il].player_name)
            for y in range(0, len(myPlayers[il].player_tiles)):
                print(y+1, ": ", myPlayers[il].player_tiles[y])
            print(y + 2, ": Turno siguiente", "\n")
            re = int(input())
            if re > y + 1:
                passs = False
            elif Game.check(mesa, myPlayers[il].player_tiles[re - 1]):
                passs = False
        if len(mesa) == 0 and re <= y + 1:
            fch = myPlayers[il].player_tiles.pop(re - 1)
            mesa.append(fch)
        elif (len(mesa) >= 1) and (re <= y+1):
            fch = myPlayers[il].player_tiles.pop(re - 1)
            k = True
            while k:
                print("Derecha (D) o izquierda (i)")
                deis = input()
                if deis == "I" or deis == "i":
                    mesa.insert(0, Game.switch(fch, mesa, deis))
                    k = False
                elif deis == "D" or deis == "d":
                    mesa.append(Game.switch(fch, mesa, deis))
                    k = False
                else:
                    k = True
        print(mesa)
    juego = Game.ganarcheck(myPlayers)
                                                        #myPlayers[il].player_tiles[re - 1].index(myPlayers[il].player_tiles[re - 1]))


#for playtiles in range(0, len(myPlayers)):
    #print(myPlayers[playtiles].player_tiles)

###