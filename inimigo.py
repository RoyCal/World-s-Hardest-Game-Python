import pygame
from settings import *
from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, x, y, speed, game):
        self.hitbox = pygame.Rect(x-15, y-15, 30, 30)
        self.game = game
        self.x = self.hitbox.x + 15
        self.y = self.hitbox.y + 15
        self.velx = speed
        self.vely = speed
        self.collided = False

    def draw(self):
        pygame.draw.circle(self.game.tela, ENEMY_COLOR, (self.x, self.y), 15)
        pygame.draw.circle(self.game.tela, "black", (self.x, self.y), 15, 6)

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
        if pygame.Rect.colliderect(self.game.player.hitbox, self.hitbox):
            self.collided = True
        else:
            self.collided = False