import math
import random

class player:
    def __init__(self, letter):
        # letter is x or o
        self,letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

class randomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.avaliable_moves())
        return square

class humanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter) 

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. input move(0-9):')
            # we're going to check that this is a correct value bt trying to cast
            # it to an integer, and if its's not. then we say its invalid
            #if that spot is not available on the board, we also sau its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print ('invalid square. try again')
        
        return val