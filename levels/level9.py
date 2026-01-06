from level import Level
from enemies.enemy3 import Enemy_3
from enemies.enemy5 import Enemy_5
from checkpoint import Checkpoint
from settings import *
from coin import Coin

class Level_9(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, 2, 2, _, _, 3, 4, 3, 4, 3, 4, _, _, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, 2, 2, _, _, 4, 3, 4, 3, 4, 3, _, _, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, 3, 4, 3, 4, 3, 4, _, _, 3, 4, _, _, 3, 4, _, _, 3, 4, _, _, _],
            [_, _, _, 4, 3, 4, 3, 4, 3, _, _, 4, 3, _, _, 4, 3, _, _, 4, 3, _, _, _],
            [_, _, _, 3, 4, _, _, _, _, _, _, 3, 4, _, _, 3, 4, _, _, 5, 5, _, _, _],
            [_, _, _, 4, 3, _, _, _, _, _, _, 4, 3, _, _, 4, 3, _, _, 5, 5, _, _, _],
            [_, _, _, 3, 4, _, _, 3, 4, 3, 4, 2, 2, 3, 4, 3, 4, _, _, _, _, _, _, _],
            [_, _, _, 4, 3, _, _, 4, 3, 4, 3, 2, 2, 4, 3, 4, 3, _, _, _, _, _, _, _],
            [_, _, _, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (218, 218)

    def __init__(self, game):
        super().__init__(game)

        self.insert_coin(Coin(1200, 720, self.game))

        self.insert_checkpoint(Checkpoint(660, 540, LADO_QUADRADINHO*2, LADO_QUADRADINHO*2, self.game))

        self.insert_enemy(Enemy_3(690, 510, 8, self.game, [(690, 510), (750, 510), (750, 360), (750, 510)]))
        self.insert_enemy(Enemy_3(1140, 750, 8, self.game, [(1140, 750), (1140, 690), (990, 690), (1140, 690)]))

        self.insert_enemy(Enemy_3(210, 330, 8, self.game, [(210, 330), (270, 330), (270, 390), (210, 390)]))
        self.insert_enemy(Enemy_3(270, 750, 8, self.game, [(270, 750), (210, 750), (210, 690), (270, 690)]))
        self.insert_enemy(Enemy_3(510, 750, 8, self.game, [(510, 750), (450, 750), (450, 690), (510, 690)]))
        self.insert_enemy(Enemy_3(510, 390, 8, self.game, [(510, 390), (450, 390), (450, 330), (510, 330)]))
        self.insert_enemy(Enemy_3(750, 270, 8, self.game, [(750, 270), (690, 270), (690, 210), (750, 210)]))
        self.insert_enemy(Enemy_3(930, 570, 8, self.game, [(930, 570), (990, 570), (990, 630), (930, 630)]))
        self.insert_enemy(Enemy_3(930, 210, 8, self.game, [(930, 210), (990, 210), (990, 270), (930, 270)]))
        self.insert_enemy(Enemy_3(1230, 270, 8, self.game, [(1230, 270), (1170, 270), (1170, 210), (1230, 210)]))
        
        self.insert_enemy(Enemy_5(270, 480, self.game))
        self.insert_enemy(Enemy_5(210, 600, self.game))
        self.insert_enemy(Enemy_5(360, 330, self.game))
        self.insert_enemy(Enemy_5(450, 240, self.game))
        self.insert_enemy(Enemy_5(360, 690, self.game))
        self.insert_enemy(Enemy_5(450, 600, self.game))
        self.insert_enemy(Enemy_5(540, 570, self.game))
        self.insert_enemy(Enemy_5(630, 630, self.game))
        self.insert_enemy(Enemy_5(600, 270, self.game))
        self.insert_enemy(Enemy_5(690, 360, self.game))
        self.insert_enemy(Enemy_5(1080, 270, self.game))
        self.insert_enemy(Enemy_5(1170, 360, self.game))
        self.insert_enemy(Enemy_5(990, 360, self.game))
        self.insert_enemy(Enemy_5(930, 480, self.game))
        self.insert_enemy(Enemy_5(930, 720, self.game))