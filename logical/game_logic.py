from logical.player import Player


class Game:
    def __init__(self, name, tiles, score, amount):
        self.player_name = name
        self.player_tiles = tiles
        self.player_score = score
        self.players_amount = amount

#EL JUEGO ACABA CUANDO EL JUGADOR SE QUEDA SIN TURNOS, TRADUCE A MANO EN EL CODIGO ANTERIOR

    def player_turns(self):


    def game(self):
        for player_number in range(0, self.players_amount):
            print ("Jugador", player_number + 1)

            for turns in range(0, self.players_amount):
                print((turns + 1), ':', )