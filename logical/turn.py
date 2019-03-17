#from logical2.player import Player
#LOGICA PARA LOS TURNOS v1.0


## METODO DE ORDENAMIENTO, QUICK SORT
def sorting(any_list):
    if len(any_list) <= 1:
        return any_list
    else:
        print any_list[0]
        return sorting([e for e in any_list[1:] if e <= any_list[0]]) + [any_list[0]] + sorting(
            [e for e in any_list[1:] if e > any_list[0]])


class Turn:

    def __init__(self, players):
        self.player_list = players

##LA FICHA MAS ALTA
    def highest_tile(self):
        all_tiles, sum_aux = [], []
        for single_player in self.player_list:
            for single_tile in single_player.player_tiles:
                if single_tile[0] == single_tile[1]:
                    sum_aux.append(single_tile[0] + single_tile[1])
            all_tiles.append([self.player_list.index(single_player), sorting(sum_aux)[len(sum_aux)-1]])
        index, value = max(all_tiles, key=lambda item: item[1])
        return index

## CHEQUEA SI HAY UN DOBLE
    def check_double(self):
        for tile_hand in self.player_list:
            if [6,6] in tile_hand.player_tiles:
                return tile_hand.index()
        return False

### SI HAY 4 JUGADORES
    def check_players(self):
        if len(self.player_list) == 4:
            return True
        return False

    def get_turn(self):
        if Turn.check_players(self):
            board = [0, 1, 2, 3]  # MANO
            if not Turn.check_double(self):
                first_turn = board[Turn.highest_tile(self)]
                del board[first_turn]
                board = sorting(board)
                board.insert(0, first_turn)

            first_turn = Turn.check_double(self)
            del board[first_turn]
            board = sorting(board)
            board.insert(0, first_turn)

        if Turn.check_double(self):
            first_turn = Turn.highest_tile(self)
            if first_turn == 0:
                board = [0, 1]
                return board
            else:
                board = [1, 0]
                return board

        highest_tile = []
        player_list = []

        for player in self.player_list:
            for tile in player.player_tiles:
                highest_tile.append(sum(tile))
            player_list.append([self.player_list.index(player), sorting(highest_tile)[len(highest_tile)-1]])
        index, value = max(player_list, key=lambda item: item[1])

        if index == 0:
            board = [0,1]
            return board

        else:
            board = [1,0]
            return board


