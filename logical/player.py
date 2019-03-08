from logical.turn import Turn

class Player:

    def __init__(self, name, tiles, score, turn):
        self.player_name = name
        self.player_tiles = tiles
        self.player_score = score
        self. player_turn = turn

    def show_tiles(self):
        print self.player_tiles
