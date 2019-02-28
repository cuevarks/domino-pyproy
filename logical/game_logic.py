class Game:
    def __init__(self, ):
        self.player_name = name
        self.player_tiles = tiles
        self.player_score = score


    def check_tranc(a, b):
        u = 0
        for f in b:
            for i in range(0, len(f)):
                if a[0][0] == f[i][0] or a[len(a) - 1][1] == f[i][0] or a[0][0] == f[i][1] or a[len(a) - 1][1] == f[i][
                    1]:
                    u += 1
        if u > 0:
            return False
        else:
            return True