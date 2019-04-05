from logical.player import Player
from logical.tiles import Tiles
from logical.game_logic import Game
myPlayers,  constraint = [], True
name = [0,0,0,0]
Domino = []
Domino = Tiles.fichama(Domino)
def ifmi(a):
    if a == 2:
        return 14
    else:
        return 7


def constraints(input_value):
    if isinstance(input_value, int):
        return False
    return None


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
''''
if len(aux) == 4:
    name = ["", "", "", ""]
else:
    name = ["", ""]
'''
for player_number in range(0, amount):
    mano = []
    e = 0
    name[e] = input("Nombre jugador " + str(player_number + 1) + ":\n")
    myTiles = Tiles()
    for inp in range(0, ifmi(amount)):
        a, Domino = Game.randomiz(Domino)
        mano.append(a)
    myPlayers.append(Player(name[e], mano, 0, 7))
    e += 1


def menor(self,mano,i):
    n = mano[0]
    for un in range(0, len(self)):
        if n >= mano[un]:
            n = mano[un]
            i = un
    return i
def Scoretranc(self):
    p, n, i = 0, 0, 0
    tur = [0, 0, 0, 0]
    mano = [0, 0, 0, 0]

    dic = {'player': self, 'position': tur}
    for u in range(0, len(self)):
        for i in range(0, len(self[u].player_tiles)):
            p = dic['player'][u].player_tiles[i][0] + dic['player'][u].player_tiles[i][1] + p
        '''.self[u].player_tiles[i][0] + self[u].player_tiles[i][1] + p '''
        dic['position'][u] = u
        mano[u] = p
        print(p)
        p = 0
    return menor(self, mano, i)


print(Scoretranc(myPlayers))


def fichama():
    mano = []
    for i in range(0,7):
        for e in range(i,7):
            mano.append([i,e])
    return mano

print(fichama())

'''
class Score(object):
    def __init__(self):
        self.tiles_hand = []

    def Scoretranc(self):
        p = 0
        mano = [0,0,0,0]
        for u in range(0, len(self)):
            for i in range(0, len(self[u].player_tiles)):
                p = self[u].player_tiles[i][0] + self[u].player_tiles[i][1]
            mano[u] = p
        return mano
'''





