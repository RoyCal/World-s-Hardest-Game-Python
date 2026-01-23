from level import Level
from enemies.enemy5 import Enemy_5
from enemies.enemy3 import Enemy_3
from settings import *
from coin import Coin
from checkpoint import Checkpoint

class Level_12(Level):
    def set_mini_map(self):
        _ = False 
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, 3, 2, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, 4, 2, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, _, _],
            [_, _, _, 3, 5, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 2, 2, 4, _, _, _],
            [_, _, _, 4, 5, 5, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 2, 3, _, _, _],
            [_, _, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def set_spawn_point(self):
        return (1140 - PLAYER_SIZE/2, 600 - PLAYER_SIZE/2)

    def __init__(self, game):
        super().__init__(game)

        #Linha superior de inimigos
        for i in range(225, 1245, 30):
            self.insert_enemy(Enemy_5(i, 285, self.game))

        #Linha inferior de inimigos
        for i in range(225, 1245, 30):
            self.insert_enemy(Enemy_5(i, 675, self.game))

        #coluna esquerda de inimigos
        for i in range(315, 705, 30):
             self.insert_enemy(Enemy_5(225, i, self.game))
         
        #coluna direita de inimigos
        for i in range(315, 705, 30):
             self.insert_enemy(Enemy_5(1215, i, self.game))

        #quadrilátero de inimigos acima do spawn
        for i in range(13):
            for j in range(8):
                self.insert_enemy(Enemy_5(825+i*ENEMY_SIZE, 315+j*ENEMY_SIZE, self.game))

        #linha de inimigos na esquerda superior do spawn
        for i in range(7):
            self.insert_enemy(Enemy_5(885+i*ENEMY_SIZE, 555, self.game))

        self.insert_enemy(Enemy_5(975, 585, self.game))
        self.insert_enemy(Enemy_5(1005, 585, self.game))

        #linha de inimigos na esquerda inferior do spawn
        for i in range(8):
            self.insert_enemy(Enemy_5(675+i*ENEMY_SIZE, 645, self.game))

        self.insert_enemy(Enemy_5(765, 615, self.game))
        self.insert_enemy(Enemy_5(795, 615, self.game))

        #linha de inimigos na parte superior da chegada
        for i in range(17):
            self.insert_enemy(Enemy_5(255+i*ENEMY_SIZE, 525, self.game))

        for i in range(8):
            self.insert_enemy(Enemy_5(255+i*ENEMY_SIZE, 495, self.game))

        for i in range(7):
            self.insert_enemy(Enemy_5(495+i*ENEMY_SIZE, 555, self.game))

        #quadrilátero de inimigos no fim da linha de inimigos na parte superior da chegada
        for i in range(3):
            for j in range(4):
                self.insert_enemy(Enemy_5(675+i*ENEMY_SIZE, 405+j*ENEMY_SIZE, self.game))

        self.insert_enemy(Enemy_5(735, 375, self.game))

        #linha de inimigos na parte inferior direita do checkpoint
        for i in range(10):
            self.insert_enemy(Enemy_5(375+i*ENEMY_SIZE, 405, self.game))

        for i in range(6):
            self.insert_enemy(Enemy_5(375+i*ENEMY_SIZE, 375, self.game))

        for i in range(4):
            self.insert_enemy(Enemy_5(555+i*ENEMY_SIZE, 435, self.game)) 

        #dois inimigos isolados lá em cima
        self.insert_enemy(Enemy_5(615, 315, self.game))
        self.insert_enemy(Enemy_5(645, 315, self.game))

        #dois inimigos isolados lá embaixo
        self.insert_enemy(Enemy_5(555, 585, self.game))
        self.insert_enemy(Enemy_5(585, 585, self.game))

        #L da chegada
        self.insert_enemy(Enemy_5(375, 615, self.game))
        for i in range(3):
            self.insert_enemy(Enemy_5(375+i*ENEMY_SIZE, 645, self.game))

        #inimigos móveis
        self.insert_enemy(Enemy_3(765, 285, 3, self.game, [(765, 285), (765, 675)]))
        self.insert_enemy(Enemy_3(795, 285, 3, self.game, [(795, 285), (795, 675)]))

        self.insert_enemy(Enemy_3(435, 285, 3, self.game, [(435, 285), (435, 675)]))
        self.insert_enemy(Enemy_3(465, 285, 3, self.game, [(465, 285), (465, 675)]))

        self.insert_enemy(Enemy_3(615, 675, 3, self.game, [(615, 675), (615, 285)]))
        self.insert_enemy(Enemy_3(645, 675, 3, self.game, [(645, 675), (645, 285)]))

        self.insert_enemy(Enemy_3(975, 675, 3, self.game, [(975, 675), (975, 285)]))
        self.insert_enemy(Enemy_3(1005, 675, 3, self.game, [(1005, 675), (1005, 285)]))

        self.insert_coin(Coin(630, 480, self.game))

        self.insert_checkpoint(Checkpoint(240, 300, 2*LADO_QUADRADINHO, 2*LADO_QUADRADINHO, self.game))