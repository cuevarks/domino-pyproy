# -*- coding: utf-8 -*-
""""
from logical import player as player
from logical import game_logic as game
from logical import score as score
from logical import tiles as tiles
"""
constraint, names = True, []

def constraints(input_value):
    if isinstance(input_value, int):
        return False
    return True

print ("--------- DOMINÓ ER CIBAO v1.0 ---------")

while (constraint):
    aux = input("¿Cuántos van a jugar? \n")
    if constraints(aux) or (aux != 2 and aux != 4): print("\nNúmero inválido")
    else:
        amount = aux
        constraint = False


for name in range(0, amount):
    aux = raw_input("Nombre jugador " + str(name+1) + ":\n")
    names.append(aux)







