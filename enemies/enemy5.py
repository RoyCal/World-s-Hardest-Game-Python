from enemy import Enemy
from settings import *

class Enemy_5(Enemy):
    """Enemy 5 - stays static."""
    def __init__(self, x, y, game):
        super().__init__(x, y, 0, game)

    def movement(self):
        pass