from enemy import Enemy
from settings import *

class Enemy_2(Enemy):
    def check_wall_collision(self):
        if self.hitbox.collidelist(list(self.game.current_level.wall_rects.values())) != -1:
            self.speed *= -1

    def movement(self):
        self.check_wall_collision()
        self.hitbox.y += self.speed