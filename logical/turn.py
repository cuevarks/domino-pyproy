#from logical2.player import Player
#LOGICA PARA LOS TURNOS v1.0


## METODO DE ORDENAMIENTO, QUICK SORT
def sorting(any_list):
    if any_list <= 1:
        return any_list
    else:
        return len(any_list)

        return sorting([e for e in any_list[1:] if e <= any_list[0]]) + [any_list[0]] + sorting(
            [e for e in any_list[1:] if e > any_list[0]])


class Turn:

    def __init__(self, players):
        self.player_list = players

##LA FICHA MAS ALTA
    def highest_tile(self):
        all_tiles, sum_aux = [], 0
        for single_player in self.player_list:
            for single_tile in single_player.player_tiles:
                if single_tile[0] == single_tile[1]:
                    sum_aux = single_tile[0] + single_tile[1]
            all_tiles.append([self.player_list.index(single_player), sorting(sum_aux)])
            '''[len(sum_aux)-1]])'''
        index, value = max(all_tiles, key=lambda item: item[1])
        return index
## CHEQUEA SI HAY UN DOBLE

    def check_double(self):
        x = 0
        for tile_hand in self:
            if [6, 6] in tile_hand.player_tiles:
                return x
            x += 1
        return False
    def switch(self):
        sw = Turn.check_double(self)
        self[sw], self[0] = self[0], self[sw]
        return self

### SI HAY 4 JUGADORES

    def check_players(self):
        if len(self.player_list) == 4:
            return True
        return False

    def get_turn(self):
        if Turn.check_players(self):
            board = [0, 1, 2, 3]  # MANO
            if not Turn.check_double:
                first_turn = board[Turn.highest_tile(self)]
                del board[first_turn]
                board = sorting(board)
                board.insert(0, first_turn)

            first_turn = Turn.check_double
            del board[first_turn]
            board = sorting(board)
            board.insert(0, first_turn)

        first_turn = Turn.highest_tile(self)
        if first_turn == 0:
            board = [0, 1]

        board = [1, 0]
        return board

    def turn_o(self):
        x = Turn.check_double
        return x
        mano = [0, 0, 0, 0]
        if x % 2 == 0:
            mano[0] = self.player_list[x]
            if x == 0:
                mano[2] = self.player_list[2]
                mano[1] = self.player_list[1]
                mano[3] = self.player_list[3]
            else:
                mano[2] = self.player_list[0]
                mano[1] = self.player_list[1]
                mano[3] = self.player_list[3]
        else:
            mano[0] = self.player_list[x]
            if x == 1:
                mano[1] = self.player_list[0]
                mano[2] = self.player_list[3]
                mano[3] = self.player_list[2]
            else:
                mano[1] = self.player_list[0]
                mano[2] = self.player_list[1]
                mano[3] = self.player_list[2]


        return self.player_list