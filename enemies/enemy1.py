from enemy import Enemy
from settings import *

class Enemy_1(Enemy):
    def check_wall_collision(self, dx, dy):
        if self.hitbox.collidelist(list(self.game.current_level.wall_rects.values())) != -1:
            self.velx *= -1

    def movement(self):
        self.check_wall_collision(self.velx, 0)
        self.hitbox.x += self.velx