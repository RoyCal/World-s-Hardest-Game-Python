import pygame as pg
from settings import *

class Coin:
    def __init__(self, x, y, game):
        self.hitbox = pg.Rect(x-COIN_SIZE/2, y-COIN_SIZE/2, COIN_SIZE, COIN_SIZE)
        self.game = game
        (self.x, self.y) = self.hitbox.center
        self.collected = False

    def draw(self):
        if not self.collected:
            pg.draw.circle(self.game.overlay, COIN_COLOR, (self.x, self.y), COIN_SIZE/2)
            pg.draw.circle(self.game.overlay, "black", (self.x, self.y), COIN_SIZE/2, 8)

    def check_player_collision(self):
        if pg.Rect.colliderect(self.game.player.hitbox, self.hitbox):
            self.collected = True

    def reset(self):
        self.collected = False

    def update(self):
        self.check_player_collision()