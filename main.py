import pygame as pg
from pygame.locals import *
from sys import exit 
from settings import *
from map import *
from player import *
from inimigo import *

class Game:
    def __init__(self):
        self.tela = pg.display.set_mode((LARGURA, ALTURA))
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(200, 300, self)
        self.inimigos = [Enemy(990, 390, -8, 1, self),
                        Enemy(990, 510, -8, 1, self),
                        Enemy(450, 450, 8, 1, self),
                        Enemy(450, 570, 8, 1, self)
                        ]

    def update(self):
        pg.display.update()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.player.update()
        for inimigo in self.inimigos:
            inimigo.update()

    def draw(self):
        self.tela.fill(BACKGROUND_COLOR)
        self.map.draw()
        self.player.draw()
        for inimigo in self.inimigos:
            inimigo.draw()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                exit()
            
            if event.type == MOUSEBUTTONDOWN:
                self.print_mouse_coord()

    def print_mouse_coord(self):
        mouse = pygame.mouse.get_pos()
        print("X: ", mouse[0])
        print("Y: ", mouse[1])

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()