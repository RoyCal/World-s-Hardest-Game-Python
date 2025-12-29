from enemy import Enemy
from settings import *
from math import hypot

# 630, 390
# 810, 390
# 810, 570
# 630, 570

class Enemy_3(Enemy):
    def __init__(self, x, y, speed, game, path):
        super().__init__(x, y, speed, game)

        self.path = path            
        self.target_index = 0

    def movement(self):
        if self.target_index >= len(self.path):
            self.target_index = 0

        target_x, target_y = self.path[self.target_index]

        # vetor direção
        dx = target_x - self.x
        dy = target_y - self.y

        distance = hypot(dx, dy)

        # chegou no ponto
        if distance < self.speed:
            self.x = target_x
            self.y = target_y
            self.target_index += 1
            return

        # normaliza o vetor
        dx /= distance
        dy /= distance

        # move
        self.hitbox.x += dx * self.speed
        self.hitbox.y += dy * self.speed