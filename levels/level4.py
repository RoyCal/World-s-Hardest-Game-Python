from level import Level
from coin import Coin
from settings import *
from enemies.enemy3 import Enemy_3

class Level_4(Level):
    def set_mini_map(self): # in the original game, level 3 has a bug where the player goes through walls. This is what made the level possible to be completed. 
        _ = False           # on this version, the walls are correctly implemented, so the map was slightly changed to make the level completable.
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 4, 3, 4, 3, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, 5, 5, 5, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, 5, 5, 5, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 3, 4, 3, 4, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (720-PLAYER_SIZE/2, 200-PLAYER_SIZE/2)
    
    def finish_level(self):
        if self.game.player.hitbox.collidelist(list(self.finish_rects.values())) != -1:
            if all(coin.collected for coin in self.coins):
                self.finished = True
                self.game.advance_level()

    def __init__(self, game):
        super().__init__(game)

        self.insert_coin(Coin(720, 360, self.game))
        self.insert_coin(Coin(900, 540, self.game)) 
        self.insert_coin(Coin(720, 720, self.game))