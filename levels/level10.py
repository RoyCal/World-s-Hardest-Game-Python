from level import Level
from enemies.enemy3 import Enemy_3
from checkpoint import Checkpoint
from settings import *
from coin import Coin

class Level_10(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 2, 2, 2, _, 5, 5, 5, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 2, 2, 2, _, 5, 5, 5, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 3, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 4, 3, _, 3, 4, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 3, 4, _, 4, 3, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 4, 3, _, 3, 4, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, 3, 4, 3, 4, _, 4, 3, 4, 3, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, 4, 3, _, _, _, _, _, 3, 4, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 4, 3, 4, 3, 4, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (550, 220)
    
    def insert_enemy_horizontal(self, x, y, speed):
        if speed > 0:
            self.insert_enemy(Enemy_3(x - ENEMY_SIZE/2 , y, speed, self.game, [(x - ENEMY_SIZE/2 , y), (x + LADO_QUADRADINHO*2 - ENEMY_SIZE*1.5, y)]))
        else:
            self.insert_enemy(Enemy_3(x + ENEMY_SIZE/2 , y, -speed, self.game, [(x + ENEMY_SIZE/2 , y), (x - LADO_QUADRADINHO*2 + ENEMY_SIZE*1.5, y)]))

    def insert_enemy_vertical(self, x, y, speed):
        if speed > 0:
            self.insert_enemy(Enemy_3(x, y - ENEMY_SIZE/2 , speed, self.game, [(x, y - ENEMY_SIZE/2 ), (x, y + LADO_QUADRADINHO*2 - ENEMY_SIZE*1.5)]))
        else:
            self.insert_enemy(Enemy_3(x, y + ENEMY_SIZE/2 , -speed, self.game, [(x, y + ENEMY_SIZE/2 ), (x, y - LADO_QUADRADINHO*2 + ENEMY_SIZE*1.5)]))

    def __init__(self, game):
        super().__init__(game)
    
        self.insert_enemy_horizontal(570, 390, -3)
        self.insert_enemy_horizontal(510, 450, 3)
        self.insert_enemy_horizontal(570, 510, -3)
        self.insert_enemy_horizontal(510, 570, 3)
        self.insert_enemy_horizontal(390, 570, 3)
        self.insert_enemy_horizontal(450, 630, -3)
        self.insert_enemy_horizontal(390, 690, 3)
        self.insert_enemy_horizontal(870, 690, -3)
        self.insert_enemy_horizontal(810, 630, 3)
        self.insert_enemy_horizontal(870, 570, -3)
        self.insert_enemy_horizontal(750, 570, -3)
        self.insert_enemy_horizontal(690, 510, 3)
        self.insert_enemy_horizontal(750, 450, -3)
        self.insert_enemy_horizontal(690, 390, 3)

        self.insert_enemy_vertical(510, 690, 3)
        self.insert_enemy_vertical(570, 750, -3)
        self.insert_enemy_vertical(630, 690, 3)
        self.insert_enemy_vertical(690, 750, -3)
        self.insert_enemy_vertical(750, 690, 3)
