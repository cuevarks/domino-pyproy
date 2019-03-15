# -*- coding: utf-8 -*-

from logical.player import Player
from logical.game_logic import Game
#from logical.score import
from logical.tiles import Tiles

constraint, names, myPlayers = True, [], []


def constraints(input_value):
    if isinstance(input_value, int):
        return False
    return True

print ("--------- DOMINÓ ER CIBAO v1.1 ---------")

while constraint:
    aux = input("¿Cuántos van a jugar? \n")
    if constraints(aux) or (aux != 2 and aux != 4): print("\nNúmero inválido")
    else:
        amount = aux
        constraint = False

for player_number in range(0, amount):
    name = raw_input("Nombre jugador " + str(player_number + 1) + ":\n")
    myPlayers.append(Player(name, Tiles, 0))

