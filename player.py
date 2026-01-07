from settings import *
import pygame as pg

class Player:
    def __init__(self, x, y, game):
        self.hitbox = pg.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        (self.x, self.y) = self.hitbox.topleft
        self.game = game
        self.image = pg.Surface((LARGURA, ALTURA), pg.SRCALPHA)
        self.dying = False
        self.alpha = 255

    def draw(self):
        pg.draw.rect(self.image, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
        pg.draw.rect(self.image, "black", (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE), 8)

        self.game.tela.blit(self.image, (0, 0))

    def movement(self):
        if self.dying:
            return
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
        self.dying = False

    def dying_animation(self):
        self.alpha -= 5
        self.image.set_alpha(self.alpha)
        if self.alpha <= 0:
            self.alpha = 255
            self.image.set_alpha(self.alpha)
            self.game.current_level.reset_coins()
            self.spawn(*self.game.current_level.active_checkpoint)

    def die(self):
        if self.dying:
            self.dying_animation()
            return
        for inimigo in self.game.current_level.enemies:
            if inimigo.collided:
                self.game.sound.player_dying.play()
                self.dying = True
    
    def update(self):
        self.image.fill((0, 0, 0, 0))
        self.movement()
        self.die()

        (self.x, self.y) = self.hitbox.topleft