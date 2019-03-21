# -*- coding: utf-8 -*-

from logical.player import Player
from logical.turn import Turn
import logical.turn
#from logical.game_logic import Game
#from logical2.score import
from logical.tiles import Tiles

constraint, names, myPlayers, myTurns, turnList = True, [], [], [], []


def constraints(input_value):
    if isinstance(input_value, int):
        return False
    return None

print ("--------- DOMINÓ ER CIBAO v1.1 ---------")


while constraint:

    aux = raw_input("¿Cuántos van a jugar? \n")
    if constraints(aux):
        print("\n Introduzca un numero")
        break
    aux = int(aux)
    if (aux != 2 and aux != 4):
        print("\nNúmero inválido")
    else:
        amount = aux
        constraint = False

for player_number in range(0, amount):
    name = raw_input("Nombre jugador " + str(player_number + 1) + ":\n")
    myTiles = Tiles()
    myPlayers.append(Player(name, myTiles.tiles_distribution(), 0))
#
# myTurns = Turn(myPlayers)
# turnList = myTurns.get_turn()
# #
print myPlayers[0].player_tiles
