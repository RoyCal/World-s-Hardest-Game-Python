from level import Level
from coin import Coin
from settings import *
from enemies.enemy3 import Enemy_3

class Level_3(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 4, 3, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 3, 4, 3, 4, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 4, 5, 5, 3, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 3, 5, 5, 4, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 4, 3, 4, 3, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (720-PLAYER_SIZE/2, 480-PLAYER_SIZE/2)
    
    def finish_level(self):
        if self.game.player.hitbox.collidelist(list(self.finish_rects.values())) != -1:
            if all(coin.collected for coin in self.coins):
                self.finished = True
                self.game.advance_level()

    def __init__(self, game):
        super().__init__(game)

        enemy_trajectorie_left = [(630, 390), (810, 390), (810, 570), (630, 570)]
        enemy_trajectorie_up = [(810, 390), (810, 570), (630, 570), (630, 390)]
        enemy_trajectorie_right = [(810, 570), (630, 570), (630, 390), (810, 390)]
        enemy_trajectorie_down = [(630, 570), (630, 390), (810, 390), (810, 570)]

        self.insert_enemy(Enemy_3(630, 570, 4, self.game, enemy_trajectorie_left))
        self.insert_enemy(Enemy_3(630, 510, 4, self.game, enemy_trajectorie_left))
        self.insert_enemy(Enemy_3(630, 450, 4, self.game, enemy_trajectorie_left))

        self.insert_enemy(Enemy_3(690, 390, 4, self.game, enemy_trajectorie_up))
        self.insert_enemy(Enemy_3(750, 390, 4, self.game, enemy_trajectorie_up))
        self.insert_enemy(Enemy_3(810, 390, 4, self.game, enemy_trajectorie_up))

        self.insert_enemy(Enemy_3(810, 450, 4, self.game, enemy_trajectorie_right))
        self.insert_enemy(Enemy_3(810, 510, 4, self.game, enemy_trajectorie_right))
        self.insert_enemy(Enemy_3(810, 570, 4, self.game, enemy_trajectorie_right))

        self.insert_enemy(Enemy_3(750, 570, 4, self.game, enemy_trajectorie_down))
        self.insert_enemy(Enemy_3(690, 570, 4, self.game, enemy_trajectorie_down))

        self.insert_coin(Coin(630, 330, self.game))