from level import Level
from enemies.enemy4 import Enemy_4
from enemies.enemy5 import Enemy_5
from enemies.enemy3 import Enemy_3
from settings import *

class Level_14(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5, 5, 5, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5, 5, 5, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5, 5, 5, _, _, _],
            [_, _, _, 2, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, 2, 2, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, 2, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (270 - PLAYER_SIZE/2, 570 - PLAYER_SIZE/2)
    
    def insert_enemy_windmill(self, x, y):
        self.insert_enemy(Enemy_5(x, y, self.game))
        self.insert_enemy(Enemy_4(x+33, y, -3, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x+66, y, -3, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x-33, y, -3, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x-66, y, -3, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y+33, -3, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y+66, -3, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y-33, -3, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y-66, -3, self.game, (x, y)))

    def insert_enemy_pair(self, x, y, initialDirection):
        if initialDirection == "up":
            self.insert_enemy(Enemy_3(x, y, 2, self.game, [(x, y), (x, y-120)]))
            self.insert_enemy(Enemy_3(x, y+33, 2, self.game, [(x, y+33), (x, y-120+33)]))
        else:
            self.insert_enemy(Enemy_3(x, y, 2, self.game, [(x, y), (x, y+120)]))
            self.insert_enemy(Enemy_3(x, y+33, 2, self.game, [(x, y+33), (x, y+120+33)]))

    def __init__(self, game):
        super().__init__(game)

        self.insert_enemy_windmill(450, 570)
        self.insert_enemy_windmill(690, 570)
        self.insert_enemy_windmill(930, 570)
        self.insert_enemy_windmill(1170, 570)

        self.insert_enemy_pair(570, 615, "up")
        self.insert_enemy_pair(810, 495, "down")
        self.insert_enemy_pair(1050, 615, "up")