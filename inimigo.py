import pygame
from settings import *

class Enemy:
    def __init__(self, x, y, speed, type, game):
        self.hitbox = pygame.Rect(x-15, y-15, 30, 30)
        self.game = game
        self.x = self.hitbox.x + 15
        self.y = self.hitbox.y + 15
        self.velx = speed
        self.vely = speed
        self.type = type
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

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int((self.x + dx * 3) / LADO_QUADRADINHO), int(self.y / LADO_QUADRADINHO)):
            self.velx *= -1

        if self.check_wall(int(self.x / LADO_QUADRADINHO), int((self.y + dy * 5) / LADO_QUADRADINHO)):
            self.vely *= -1

    def movement(self):
        match self.type:
            case 1:
                self.check_wall_collision(self.velx, 0)
                self.hitbox.x += self.velx

    def check_player_collision(self):
        if pygame.Rect.colliderect(self.game.player.hitbox, self.hitbox):
            self.collided = True
        else:
            self.collided = False