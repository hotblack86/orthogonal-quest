''' Enemy tiles '''

import pygame as pg
from constants import TILESIZE, RED


class Enemy(pg.sprite.Sprite):
    ''' Creates enemies '''

    def __init__(self, x_pos, y_pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = TILESIZE * x_pos
        self.rect.y = TILESIZE * y_pos