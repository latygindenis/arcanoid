# -*- coding:utf-8- -*-

from pygame.sprite import Sprite
from pygame import Surface

class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((25, 20))
        self.image.fill((255, 22, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y