import pygame as pg
from settings import *
from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, x, y, speed, game):
        self.hitbox = pg.Rect(x-ENEMY_SIZE/2, y-ENEMY_SIZE/2, ENEMY_SIZE, ENEMY_SIZE)
        self.game = game
        (self.x, self.y) = self.hitbox.center
        self.speed = speed
        self.collided = False

    def draw(self):
        pg.draw.circle(self.game.tela, ENEMY_COLOR, (self.x, self.y), ENEMY_SIZE/2)
        pg.draw.circle(self.game.tela, "black", (self.x, self.y), ENEMY_SIZE/2, 8)

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
        # ponto mais próximo do retângulo
        closest_x = max(self.game.player.hitbox.left, min(self.x, self.game.player.hitbox.right))
        closest_y = max(self.game.player.hitbox.top,  min(self.y, self.game.player.hitbox.bottom))

        # distância ao quadrado
        dx = self.x - closest_x
        dy = self.y - closest_y

        self.collided = dx*dx + dy*dy <= (ENEMY_SIZE/2-ENEMY_HITBOX_CORRECTION)*(ENEMY_SIZE/2-ENEMY_HITBOX_CORRECTION)