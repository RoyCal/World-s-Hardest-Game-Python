from level import Level
from enemies.enemy3 import Enemy_3
from coin import Coin

class Level_8(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 4, 3, 4, 3, _, _, 4, 3, 4, 3, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 3, 2, _, 4, 3, 4, 3, _, _, 4, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 4, _, _, 3, _, _, 4, _, _, 3, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 3, 4, 3, 4, _, _, 3, 4, 3, 4, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 4, _, _, 3, _, _, 4, _, _, 3, 5, 5, _, _, _, _, _],
            [_, _, _, _, _, _, _, 3, _, _, 4, _, _, 3, _, _, 4, 5, 5, _, _, _, _, _],
            [_, _, _, _, _, _, _, 4, 3, 4, 3, _, _, 4, 3, 4, 3, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 3, _, _, 4, _, _, 3, _, _, 4, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 4, _, _, 3, 4, 3, 4, _, _, 3, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, 3, 4, 3, 4, _, _, 3, 4, 3, 4, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (488, 248)

    def insert_square_path_enemy(self, x, y, speed, direction):
        if direction == 'clockwise':
            self.insert_enemy(Enemy_3(x, y, speed, self.game, [(x, y), (x + 180, y), (x + 180, y + 180), (x, y + 180)]))
        else:
            self.insert_enemy(Enemy_3(x, y, speed, self.game, [(x, y), (x - 180, y), (x - 180, y + 180), (x, y + 180)]))

    def __init__(self, game):
        super().__init__(game)

        self.insert_square_path_enemy(450, 210, 5, 'clockwise')
        self.insert_square_path_enemy(450, 390, 5, 'clockwise')
        self.insert_square_path_enemy(450, 570, 5, 'clockwise')

        self.insert_square_path_enemy(990, 210, 5, 'counterclockwise')
        self.insert_square_path_enemy(990, 390, 5, 'counterclockwise')
        self.insert_square_path_enemy(990, 570, 5, 'counterclockwise')

        self.insert_enemy(Enemy_3(630, 270, 6, self.game, [(630, 270), (810, 270), (810, 690), (630, 690)]))

        self.insert_coin(Coin(990, 210, self.game))
        self.insert_coin(Coin(990, 750, self.game))
        self.insert_coin(Coin(450, 750, self.game))