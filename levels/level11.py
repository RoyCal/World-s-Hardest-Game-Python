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
    


        self.insert_enemy(Enemy_6(680, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(680, 500, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 440, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(700, 520, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 440, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(740, 520, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(760, 460, -2, self.game, (720, 480), 800))
        self.insert_enemy(Enemy_6(760, 500, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(740, 400-40*i, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(700, 400-40*i, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(740, 560+40*i, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(700, 560+40*i, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(800+40*i, 460, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(800+40*i, 500, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(640-40*i, 500, -2, self.game, (720, 480), 800))

        for i in range(6):
            self.insert_enemy(Enemy_6(640-40*i, 460, -2, self.game, (720, 480), 800))

        self.insert_coin(Coin(510, 270, self.game))
        self.insert_coin(Coin(930, 690, self.game))
        