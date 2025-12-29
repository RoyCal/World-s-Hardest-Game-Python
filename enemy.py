import pygame as pg
from settings import *
from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, x, y, speed, game):
        self.hitbox = pg.Rect(x-ENEMY_SIZE/2, y-ENEMY_SIZE/2, ENEMY_SIZE, ENEMY_SIZE)
        self.game = game
        (self.x, self.y) = self.hitbox.center
        self.velx = speed
        self.vely = speed
        self.collided = False

    def draw(self):
        pg.draw.circle(self.game.tela, ENEMY_COLOR, (self.x, self.y), 15)
        pg.draw.circle(self.game.tela, "black", (self.x, self.y), 15, 6)

    def update(self):
        self.movement()
        self.check_player_collision()

        (self.x, self.y) = self.hitbox.center

    def check_wall(self, x, y):
        return (x, y) not in self.game.current_level.world_map

    @abstractmethod
    def movement(self):
        """Cada inimigo deve definir sua própria função de movimento"""
        pass

    def check_player_collision(self):
        if pg.Rect.colliderect(self.game.player.hitbox, self.hitbox):
            self.collided = True
        else:
            self.collided = False