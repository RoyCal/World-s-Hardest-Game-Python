from level import Level
from enemies.enemy2 import Enemy_2
from coin import Coin

class Level_7(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _],
            [_, _, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _],
            [_, _, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _],
            [_, _, _, 2, 2, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 5, 5, 5, _, _, _],
            [_, _, _, 2, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 5, 5, _, _, _],
            [_, _, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _],
            [_, _, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _, _],
            [_, _, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (200, 460)

    def __init__(self, game):
        super().__init__(game)

        self.insert_enemy(Enemy_2(390, 630, 10, self.game))
        self.insert_enemy(Enemy_2(450, 330, -10, self.game))
        self.insert_enemy(Enemy_2(510, 630, 10, self.game))
        self.insert_enemy(Enemy_2(570, 330, -10, self.game))
        self.insert_enemy(Enemy_2(630, 630, 10, self.game))
        self.insert_enemy(Enemy_2(690, 330, -10, self.game))
        self.insert_enemy(Enemy_2(750, 630, 10, self.game))
        self.insert_enemy(Enemy_2(810, 330, -10, self.game))
        self.insert_enemy(Enemy_2(870, 630, 10, self.game))
        self.insert_enemy(Enemy_2(930, 330, -10, self.game))
        self.insert_enemy(Enemy_2(990, 630, 10, self.game))
        self.insert_enemy(Enemy_2(1050, 330, -10, self.game))

        self.insert_coin(Coin(390, 270, self.game))
        self.insert_coin(Coin(390, 690, self.game))
        self.insert_coin(Coin(1050, 270, self.game))
        self.insert_coin(Coin(390, 270, self.game))
        self.insert_coin(Coin(1050, 690, self.game))