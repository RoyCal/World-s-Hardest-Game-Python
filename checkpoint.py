from settings import *
import pygame as pg

class Checkpoint:
    def __init__(self, x, y, width, height, game):
        self.hitbox = pg.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.spawn_point = (self.hitbox.centerx - PLAYER_SIZE // 2, self.hitbox.centery - PLAYER_SIZE // 2)
        self.game = game

    def update(self):
        self.check_player_collision()

    def check_player_collision(self):
        if self.hitbox.colliderect(self.game.player.hitbox):
            self.game.current_level.active_checkpoint = self.spawn_point