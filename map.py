import pygame
from settings import *

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, 4, 3, 2, 2, 2, _, _, _],
    [_, _, _, 2, 2, 2, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, 2, 2, 2, _, _, _],
    [_, _, _, 2, 2, 2, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, 2, 2, 2, _, _, _],
    [_, _, _, 2, 2, 2, _, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, _, 2, 2, 2, _, _, _],
    [_, _, _, 2, 2, 2, _, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, _, 2, 2, 2, _, _, _],
    [_, _, _, 2, 2, 2, 3, 4, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.wall_rects = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map_and_rects()

    def get_map_and_rects(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                else:
                    self.wall_rects[(i, j)] = pygame.Rect(i * LADO_QUADRADINHO, j * LADO_QUADRADINHO, LADO_QUADRADINHO, LADO_QUADRADINHO)

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

            pygame.draw.rect(self.game.tela, color, (pos[0] * LADO_QUADRADINHO, pos[1] * LADO_QUADRADINHO, LADO_QUADRADINHO, LADO_QUADRADINHO))