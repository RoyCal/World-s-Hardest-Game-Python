from level import Level
from enemies.enemy2 import Enemy_2
from coin import Coin

class Level_2(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _],
            [_, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _],
            [_, _, 2, 2, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 5, 5, 5, _, _],
            [_, _, 2, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 5, 5, _, _],
            [_, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _],
            [_, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (200, 460)
    
    def finish_level(self):
        if self.game.player.hitbox.collidelist(list(self.finish_rects.values())) != -1:
            if all(coin.collected for coin in self.coins):
                self.finished = True
                self.game.advance_level()

    def __init__(self, game):
        super().__init__(game)

        self.insert_enemy(Enemy_2(330, 330, -5, self.game))
        self.insert_enemy(Enemy_2(390, 630, 5, self.game))
        self.insert_enemy(Enemy_2(450, 330, -5, self.game))
        self.insert_enemy(Enemy_2(510, 630, 5, self.game))
        self.insert_enemy(Enemy_2(570, 330, -5, self.game))
        self.insert_enemy(Enemy_2(630, 630, 5, self.game))
        self.insert_enemy(Enemy_2(690, 330, -5, self.game))
        self.insert_enemy(Enemy_2(750, 630, 5, self.game))
        self.insert_enemy(Enemy_2(810, 330, -5, self.game))
        self.insert_enemy(Enemy_2(870, 630, 5, self.game))
        self.insert_enemy(Enemy_2(930, 330, -5, self.game))
        self.insert_enemy(Enemy_2(990, 630, 5, self.game))
        self.insert_enemy(Enemy_2(1050, 330, -5, self.game))
        self.insert_enemy(Enemy_2(1110, 630, 5, self.game)) 

        self.insert_coin(Coin(720, 480, self.game))