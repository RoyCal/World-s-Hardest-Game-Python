from level import Level
from settings import *
from enemies.enemy4 import Enemy_4
from checkpoint import Checkpoint
from coin import Coin

class Level_6(Level):
    def set_mini_map(self):
        _ = False           
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, 2, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, 2, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, 2, _, _, _],
            [_, _, _, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, 5, 5, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, 5, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (240-PLAYER_SIZE/2, 240-PLAYER_SIZE/2)
    
    def finish_level(self):
        if self.game.player.hitbox.collidelist(list(self.finish_rects.values())) != -1:
            if all(coin.collected for coin in self.coins):
                self.finished = True
                self.game.advance_level()
    
    def create_enemy_windmill(self, x, y):
        self.insert_enemy(Enemy_4(x, y, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x - 52.5, y, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x - 105, y, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x + 52.5, y, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x + 105, y, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y - 52.5, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y - 105, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y + 52.5, 2.1, self.game, (x, y)))
        self.insert_enemy(Enemy_4(x, y + 105, 2.1, self.game, (x, y)))

    def __init__(self, game):
        super().__init__(game)

        self.insert_checkpoint(Checkpoint(1020, 420, LADO_QUADRADINHO*4, LADO_QUADRADINHO*2, game))

        self.create_enemy_windmill(420, 300)
        self.create_enemy_windmill(660, 300)
        self.create_enemy_windmill(900, 300)
        self.create_enemy_windmill(1140, 300)
        self.create_enemy_windmill(420, 660)
        self.create_enemy_windmill(660, 660)
        self.create_enemy_windmill(900, 660)
        self.create_enemy_windmill(1140, 660)

        self.insert_coin(Coin(1050, 570, game))
        self.insert_coin(Coin(810, 570, game))
        self.insert_coin(Coin(570, 570, game))
        self.insert_coin(Coin(330, 570, game))