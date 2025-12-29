from settings import *
import pygame as pg

class Player:
    def __init__(self, x, y, game):
        self.hitbox = pg.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        (self.x, self.y) = self.hitbox.topleft
        self.game = game

    def draw(self):
        pg.draw.rect(self.game.tela, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
        pg.draw.rect(self.game.tela, "black", (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE), 6)

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.hitbox.y += -PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.y = self.nearest_multiple(self.hitbox.y, LADO_QUADRADINHO)
        if keys[pg.K_s]:
            self.hitbox.y += PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.y = self.nearest_multiple(self.hitbox.y, LADO_QUADRADINHO) + LADO_QUADRADINHO - PLAYER_SIZE
        if keys[pg.K_a]:
            self.hitbox.x += -PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.x = self.nearest_multiple(self.hitbox.x, LADO_QUADRADINHO)
        if keys[pg.K_d]:
            self.hitbox.x += PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.x = self.nearest_multiple(self.hitbox.x, LADO_QUADRADINHO) + LADO_QUADRADINHO - PLAYER_SIZE

    def nearest_multiple(self, a: int, b: int) -> int:
        k = round(a / b)
        return k * b

    def wall_collision(self):
        if self.hitbox.collidelist(list(self.game.current_level.wall_rects.values())) != -1:
            return True
        return False

    def spawn(self, x, y):
        self.hitbox.x = x
        self.hitbox.y = y

    def die(self):
        for inimigo in self.game.current_level.enemies:
            if inimigo.collided:
                self.game.current_level.reset_coins()
                self.spawn(*self.game.current_level.active_checkpoint)

    
    def update(self):
        self.movement()
        self.die()

        (self.x, self.y) = self.hitbox.topleft