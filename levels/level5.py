from level import Level
from settings import *
from enemies.enemy4 import Enemy_4
from checkpoint import Checkpoint

class Level_5(Level):
    def set_mini_map(self):
        _ = False           
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, _],
            [_, _, _, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, 4, _, _, _, _, _],
            [_, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, 3, _, 3, _, _, _, _, _],
            [_, _, _, _, _, 3, _, 3, 4, 3, 4, 3, 4, 3, 5, _, 4, _, 4, _, _, _, _, _],
            [_, _, _, _, _, 4, _, 4, _, 4, 3, 4, 3, 4, 5, _, 3, _, 3, _, _, _, _, _],
            [_, _, _, _, _, 3, _, 3, _, _, _, _, _, _, _, _, 4, _, 4, _, _, _, _, _],
            [_, _, _, _, _, 4, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, 3, _, _, _, _, _],
            [_, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _],
            [_, _, _, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (240-PLAYER_SIZE/2, 210-PLAYER_SIZE/2)
    
    def finish_level(self):
        if self.game.player.hitbox.collidelist(list(self.finish_rects.values())) != -1:
            self.finished = True
            self.game.advance_level()

    def __init__(self, game):
        super().__init__(game)

        self.insert_enemy(Enemy_4(810, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(630, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 570, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 390, 1.4, game, (720, 480)))

        self.insert_enemy(Enemy_4(930, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(510, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 690, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 270, 1.4, game, (720, 480)))

        self.insert_enemy(Enemy_4(1050, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(390, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 810, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 150, 1.4, game, (720, 480)))

        self.insert_enemy(Enemy_4(1170, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(250, 480, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 930, 1.4, game, (720, 480)))
        self.insert_enemy(Enemy_4(720, 30, 1.4, game, (720, 480)))

        self.insert_checkpoint(Checkpoint(1140, 180, LADO_QUADRADINHO, LADO_QUADRADINHO, (1148, 188), game))
        self.insert_checkpoint(Checkpoint(180, 300, LADO_QUADRADINHO, LADO_QUADRADINHO, (188, 308), game))