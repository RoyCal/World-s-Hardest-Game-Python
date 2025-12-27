from enemy import Enemy
from settings import *

class Enemy_2(Enemy):
    def check_wall_collision(self, dx, dy):
        if self.hitbox.collidelist(list(self.game.current_level.wall_rects.values())) != -1:
            self.vely *= -1

    def movement(self):
        self.check_wall_collision(self.velx, 0)
        self.hitbox.y += self.vely