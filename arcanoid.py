# -*- coding:utf-8 -*-

from pygame.sprite import Sprite
from pygame import image

class Arcanoid (Sprite):
    def __init__(self, x, y, ):
        Sprite.__init__(self)
        self.image = image.load('platform.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right):
        if left:
            if self.rect.x > 10:
                self.rect.x -= 2
        if right:
            if self.rect.x < 320:
                self.rect.x += 2


