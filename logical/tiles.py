import random


def player_distribution(item, player1):
    if len(player1) <= 6:
        player1.append(item)


def dom(domino):
    while len(domino) != 0:
        a = random.choice(domino)
        fd = domino.pop(domino.index(a))
        player_distribution(fd)


class Tiles(object):

    def __init__(self):
        self.tiles_hand = []

    ficha = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
             [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5],
             [5, 6], [6, 6]]





    def tiles_distribution(self, domino):
        while len(self.tiles_hand) <= 6:
            self.tiles_hand.append([random.randint(0, 6), random.randint(0, 6)])

        return self.tiles_hand

    def fichama(self):
        self = []
        for i in range(0, 7):
            for e in range(i, 7):
                self.append([i, e])
        return self
'''
ficha = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2],
         [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]

domino = ficha

def player_distribution(item):
    if len(player1) <= 6:
        player1.append(item)
    elif len(player2) <= 6:
        player2.append(item)
    elif len(player3) <= 6:
        player3.append(item)
    else:
        player4.append(item)

while len(domino) != 0:
    a = random.choice(domino)
    fd = domino.pop(domino.index(a))
    player_distribution(fd)
'''
