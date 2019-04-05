from logical.player import Player

import random

class Game:
    def __init__(self, name, tiles, score, amount):
        self.player_name = name
        self.player_tiles = tiles
        self.player_score = score
        self.players_amount = amount

#EL JUEGO ACABA CUANDO EL JUGADOR SE QUEDA SIN TURNOS, TRADUCE A MANO EN EL CODIGO ANTERIOR

    def player_turns(self):
        return self

    def game(self):
        for player_number in range(0, self.players_amount):
            print ("Jugador", player_number + 1)

            for turns in range(0, self.players_amount):
                print((turns + 1), ':', )

    def check(mesa, fh):
        if fh == [6, 6] and len(mesa) == 0:
            return True
        if len(mesa) != 0:
            if mesa[0][0] == fh[0] or mesa[len(mesa) - 1][1] == fh[0] or mesa[0][0] == fh[1] or mesa[len(mesa) - 1][1] == fh[1]:
                return True
        else:
            return False

    def ganarcheck(self):
        if len(self) == 4:
            if len(self[0].player_tiles) == 0 or len(self[1].player_tiles) == 0 or len(self[2].player_tiles) == 0 or len(self[3].player_tiles) == 0:
                return False
        elif len(self) == 2:
            if len(self[0].player_tiles) == 0 or len(self[1].player_tiles) == 0:
                return False
        return True

    def check2(mesa, fh):
        m = ""
        if len(mesa) != 0:
            if ((mesa[0][0] == fh[0]) or (mesa[0][0] == fh[1])) and ((mesa[len(mesa) - 1][1] == fh[0]) or (mesa[len(mesa) - 1][1] == fh[1])):
                m = "di"
            elif (mesa[len(mesa) - 1][1] == fh[0]) or (mesa[len(mesa) - 1][1] == fh[1]):
                m = "d"
            elif (mesa[0][0] == fh[0]) or (mesa[0][0] == fh[1]):
                m = "i"
        return m

    def empty(self):
        for a in range(0, len(self)):
            del self[a].player_tiles[:]
        return self

    def randomiz(domino):
        a = random.choice(domino)
        fd = domino.pop(domino.index(a))
        return fd, domino

