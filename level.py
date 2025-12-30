import pygame as pg
from settings import *
from abc import ABC, abstractmethod

class Level(ABC):
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.coins = []
        self.checkpoints = []
        self.world_map = {}
        self.wall_rects = {}
        self.finish_rects = {}
        self.finished = False

        self.mini_map = self.set_mini_map()
        self.spawn_point = self.set_spawn_point()
        self.set_map_and_rects()

        self.active_checkpoint = self.spawn_point

    @abstractmethod
    def set_mini_map(self):
        """Cada nível deve definir seu próprio mini_map"""
        pass

    @abstractmethod
    def set_spawn_point(self):
        """Cada nível deve definir seu próprio ponto de spawn"""
        pass

    @abstractmethod
    def finish_level(self):
        """Cada nível deve definir sua própria função de finalização"""
        pass

    def update(self):
        self.finish_level()

    def set_map_and_rects(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    if value == 5:
                        self.finish_rects[(i, j)] = pg.Rect(i * LADO_QUADRADINHO, j * LADO_QUADRADINHO, LADO_QUADRADINHO, LADO_QUADRADINHO)
                    self.world_map[(i, j)] = value
                else:
                    self.wall_rects[(i, j)] = pg.Rect(i * LADO_QUADRADINHO, j * LADO_QUADRADINHO, LADO_QUADRADINHO, LADO_QUADRADINHO)
    
    def insert_enemy(self, enemy):
        self.enemies.append(enemy)

    def insert_coin(self, coin):
        self.coins.append(coin)
    
    def insert_checkpoint(self, checkpoint):
        self.checkpoints.append(checkpoint)

    def reset_coins(self):
        for coin in self.coins:
            coin.collected = False

    def draw(self):
        for pos in self.world_map:
            valor = self.world_map[(pos[0], pos[1])]

            match valor:
                case 1: # barra superior e inferior
                    color = "black"
                case 2: # spawn
                    color = SAFEZONE_COLOR
                case 3: # quadradinho claro
                    color = QUADRADINHO_CLARO_COLOR
                case 4: # quadradinho escuro
                    color = QUADRADINHO_ESCURO_COLOR
                case 5: # chegada
                    color = SAFEZONE_COLOR

            pg.draw.rect(self.game.tela, color, (pos[0] * LADO_QUADRADINHO, pos[1] * LADO_QUADRADINHO, LADO_QUADRADINHO, LADO_QUADRADINHO))