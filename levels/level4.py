from level import Level
from coin import Coin
from settings import *
from enemies.enemy4 import Enemy_4

class Level_4(Level):
    def set_mini_map(self):
        _ = False           
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

        self.insert_enemy(Enemy_4(570, 390, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(600, 420, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(630, 450, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(660, 480, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(690, 510, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(720, 540, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(750, 570, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(780, 600, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(810, 630, 2, self.game, (720, 540)))  
        self.insert_enemy(Enemy_4(840, 660, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(870, 690, 2, self.game, (720, 540)))  
        self.insert_enemy(Enemy_4(870, 390, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(840, 420, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(810, 450, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(780, 480, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(750, 510, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(690, 570, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(660, 600, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(630, 630, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(600, 660, 2, self.game, (720, 540)))
        self.insert_enemy(Enemy_4(570, 690, 2, self.game, (720, 540)))