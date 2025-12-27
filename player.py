from settings import *
import pygame

class Player:
    def __init__(self, x, y, game):
        self.hitbox = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.x = self.hitbox.x
        self.y = self.hitbox.y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.tela, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
        pygame.draw.rect(self.game.tela, "black", (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE), 6)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y += -PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.y = self.nearest_multiple(self.hitbox.y, LADO_QUADRADINHO)
        if keys[pygame.K_s]:
            self.hitbox.y += PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.y = self.nearest_multiple(self.hitbox.y, LADO_QUADRADINHO) + LADO_QUADRADINHO - PLAYER_SIZE
        if keys[pygame.K_a]:
            self.hitbox.x += -PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.x = self.nearest_multiple(self.hitbox.x, LADO_QUADRADINHO)
        if keys[pygame.K_d]:
            self.hitbox.x += PLAYER_SPEED
            if self.wall_collision():
                self.hitbox.x = self.nearest_multiple(self.hitbox.x, LADO_QUADRADINHO) + LADO_QUADRADINHO - PLAYER_SIZE

    def nearest_multiple(self, a: int, b: int) -> int:
        k = round(a / b)
        return k * b

    def wall_collision(self):
        if self.hitbox.collidelist(list(self.game.map.wall_rects.values())) != -1:
            return True
        return False

    def spawn(self, x, y):
        self.hitbox.x = x
        self.hitbox.y = y

    def die(self):
        for inimigo in self.game.inimigos:
            if inimigo.collided:
                self.spawn(200, 300)
    
    def update(self):
        self.movement()
        self.die()

        (self.x, self.y) = self.hitbox.topleft