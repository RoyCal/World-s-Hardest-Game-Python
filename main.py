import pygame as pg
from pygame.locals import *
from sys import exit 
from settings import *
from levels.level1 import Level_1
from levels.level2 import Level_2
from levels.level3 import Level_3
from levels.level4 import Level_4
from player import Player

class Game:
    def __init__(self):
        self.tela = pg.display.set_mode((LARGURA, ALTURA))
        self.clock = pg.time.Clock()
        self.levels = [Level_1, Level_2, Level_3, Level_4]
        self.current_level = None
        self.new_game()

    def new_game(self):
        self.current_level = Level_4(self)
        self.player = Player(*self.current_level.spawn_point, self)

    def advance_level(self):
        try:
            self.current_level = self.levels[self.levels.index(type(self.current_level)) + 1](self)
        except:
            self.current_level = self.levels[0](self)
        self.player.spawn(*self.current_level.spawn_point)

    def update(self):
        pg.display.update()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.player.update()
        self.current_level.update()
        for inimigo in self.current_level.enemies:
            inimigo.update()
        for coin in self.current_level.coins:
            coin.update()

    def draw(self):
        self.tela.fill(BACKGROUND_COLOR)
        self.current_level.draw()
        self.player.draw()
        for inimigo in self.current_level.enemies:
            inimigo.draw()
        for coin in self.current_level.coins:
            coin.draw()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                exit()
            
            if event.type == MOUSEBUTTONDOWN:
                self.print_mouse_coord()

    def print_mouse_coord(self):
        mouse = pg.mouse.get_pos()
        print(f"X: {mouse[0]}, Y: {mouse[1]}")

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.print_mouse_coord()

if __name__ == "__main__":
    game = Game()
    game.run()