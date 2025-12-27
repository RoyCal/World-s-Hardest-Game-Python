from inimigo import *

class Enemy_1(Enemy):
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int((self.x + dx * 3) / LADO_QUADRADINHO), int(self.y / LADO_QUADRADINHO)):
            self.velx *= -1

        if self.check_wall(int(self.x / LADO_QUADRADINHO), int((self.y + dy * 5) / LADO_QUADRADINHO)):
            self.vely *= -1

    def movement(self):
        self.check_wall_collision(self.velx, 0)
        self.hitbox.x += self.velx