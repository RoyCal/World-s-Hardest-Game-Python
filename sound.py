import pygame as pg
from settings import *

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.main_theme = pg.mixer.Sound("sounds/main-theme-music.mp3")
        self.player_dying = pg.mixer.Sound("sounds/player_dying.mp3")
        self.coin_collect = pg.mixer.Sound("sounds/coin_capture.mp3")
        self.level_complete = pg.mixer.Sound("sounds/level_complete.mp3")

        self.main_theme.set_volume(MAIN_THEME_VOLUME)
        self.player_dying.set_volume(SFX_VOLUME)
        self.coin_collect.set_volume(SFX_VOLUME)
        self.level_complete.set_volume(SFX_VOLUME)