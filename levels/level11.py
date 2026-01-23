from level import Level
from enemies.enemy6 import Enemy_6
from settings import *
from coin import Coin

class Level_11(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _],
            [_, _, _, _, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, _, _, 4, 3, _, _, _, _],
            [_, _, _, _, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, _, _, 2, 2, _, _, _, _],
            [_, _, _, _, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, _, _, 2, 2, _, _, _, _],
            [_, _, _, _, 5, 5, _, _, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _, _, _],
            [_, _, _, _, 5, 5, _, _, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _, _, _],
            [_, _, _, _, 3, 4, _, _, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _, _, _],
            [_, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (1140 - PLAYER_SIZE/2, 420 - PLAYER_SIZE/2)

    def __init__(self, game):
        super().__init__(game)
    
        self.insert_enemy(Enemy_6(740, 440, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(760, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(680, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 520, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 440, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(680, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(760, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 520, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(740, 400, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 360, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 320, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 280, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 240, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 200, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(700, 400, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 360, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 320, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 280, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 240, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 200, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(740, 560, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 600, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 640, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 680, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 720, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 760, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(700, 560, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 600, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 640, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 680, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 720, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 760, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(800, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(840, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(880, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(920, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(960, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(1000, 460, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(800, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(840, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(880, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(920, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(960, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(1000, 500, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(640, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(600, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(560, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(520, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(480, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(440, 500, -2, self.game, (720, 480), 800))

        self.insert_enemy(Enemy_6(640, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(600, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(560, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(520, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(480, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(440, 460, -2, self.game, (720, 480), 800))

        self.insert_coin(Coin(510, 270, self.game))
        self.insert_coin(Coin(930, 690, self.game))
        