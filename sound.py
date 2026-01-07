import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.main_theme = pg.mixer.Sound("sounds/main-theme-music.mp3")
        self.player_dying = pg.mixer.Sound("sounds/player_dying.mp3")
        self.coin_collect = pg.mixer.Sound("sounds/coin_capture.mp3")
        self.level_complete = pg.mixer.Sound("sounds/level_complete.mp3")