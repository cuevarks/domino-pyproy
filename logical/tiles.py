import random


class Tiles:

    def __init__(self):
        self.tiles_hand = []

    def tiles_distribution(self):
        while len(self.tiles_hand) <= 6:
            self.tiles_hand.append([random.randint(0, 6), random.randint(0, 6)])