import pygame as pg
from settings import *
from abc import ABC, abstractmethod

class Level(ABC):
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.world_map = {}
        self.wall_rects = {}

        self.mini_map = self.get_mini_map()
        self.get_map_and_rects()

    @abstractmethod
    def get_mini_map(self):
        """Cada nível deve definir seu próprio mini_map"""
        pass

    def get_map_and_rects(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                else:
                    self.wall_rects[(i, j)] = pg.Rect(i * LADO_QUADRADINHO, j * LADO_QUADRADINHO, LADO_QUADRADINHO, LADO_QUADRADINHO)
    
    def insert_enemy(self, enemy):
        self.enemies.append(enemy)

    def draw(self):
        for pos in self.world_map:
            valor = self.world_map[(pos[0], pos[1])]

            match valor:
                case 1:
                    color = "black"
                case 2:
                    color = SAFEZONE_COLOR
                case 3:
                    color = QUADRADINHO_CLARO_COLOR
                case 4:
                    color = QUADRADINHO_ESCURO_COLOR

            pg.draw.rect(self.game.tela, color, (pos[0] * LADO_QUADRADINHO, pos[1] * LADO_QUADRADINHO, LADO_QUADRADINHO, LADO_QUADRADINHO))