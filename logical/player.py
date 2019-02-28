class Player:

    def __init__(self, name, tiles, score):
        self.player_name = name
        self.player_tiles = tiles
        self.player_score = score

    def show_tiles(self):
        print self.player_tiles
