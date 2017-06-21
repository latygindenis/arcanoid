# -*- coding:utf-8 -*-

from pygame.sprite import Sprite, collide_rect
from pygame import image
import random

class Ball(Sprite):

    go_right = True
    go_left = False
    go_down = True
    go_up = False
    Vel_y = 1.0

    def Intersect(x1, x2, y1, y2, db1, db2):
        if (x1 > x2 - db1) and (x1 < x2 + db2) and (y1 > y2 - db1) and (y1 < y2 + db2):
            return 1
        else:
            return 0

    def __init__(self, x, y, ):
        Sprite.__init__(self)
        self.image = image.load('hero.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collide(self, platforms):#Обработка столкновений с плитками
        for pl in platforms:
            if collide_rect(self, pl):
                if (pl.rect.right >= self.rect.right and Ball.go_right == True and Ball.go_up == True):
                    Ball.go_right = False
                    Ball.go_left = True
                if (pl.rect.left <= self.rect.left and Ball.go_left == True and Ball.go_up == True):
                    Ball.go_left = False
                    Ball.go_right = True
                if (pl.rect.right >= self.rect.right and Ball.go_right == True and Ball.go_down == True):
                    Ball.go_right = False
                    Ball.go_left = True
                if (pl.rect.left <= self.rect.left and Ball.go_left == True and Ball.go_down == True):
                    Ball.go_left = False
                    Ball.go_right = True

                if (pl.rect.top <= self.rect.top and Ball.go_left == True and Ball.go_up == True):
                    Ball.go_up=False
                    Ball.go_down=True
                if (pl.rect.bottom >= self.rect.bottom and Ball.go_left == True and Ball.go_down == True):
                    Ball.go_down=False
                    Ball.go_up=True
                if (pl.rect.top <= self.rect.top and Ball.go_right == True and Ball.go_up == True):
                    print(pl.rect.bottom, self.rect.top)
                    Ball.go_up = False
                    Ball.go_down = True
                if (pl.rect.bottom >= self.rect.bottom and Ball.go_right == True and Ball.go_down == True):
                    Ball.go_down = False
                    Ball.go_up = True
                pl.rect.x=-500

    def update(self, x_platform, y_platform, platforms):
        if (Ball.go_right == True and Ball.go_down == True):
            self.rect.x += 1.2
            self.rect.y += Ball.Vel_y
            if (self.rect.x> 360):
                Ball.go_right = False
                Ball.go_left = True
                Ball.Vel_y = random.uniform(1.0, 2.0)
            if (self.rect.y > 360):
                return 0
        if (Ball.go_left == True and Ball.go_down == True):
            self.rect.x -= 1.2
            self.rect.y += Ball.Vel_y
            if (self.rect.x < 10):
                Ball.go_left = False
                Ball.go_right = True
                Ball.Vel_y = random.uniform(1.0, 2.0)
            if (self.rect.y > 360):
                return 0
        if (Ball.go_right == True and Ball.go_up == True):
            self.rect.x += 1.2
            self.rect.y -= Ball.Vel_y
            if (self.rect.x > 360):
                Ball.go_right = False
                Ball.go_left = True
                Ball.Vel_y = random.uniform(1.0, 2.0)
            if (self.rect.y < 10):
                Ball.go_up = False
                Ball.go_down = True
                Ball.Vel_y = random.uniform(1.0, 2.0)
        if (Ball.go_left == True and Ball.go_up == True):
            self.rect.x -= 1.0
            self.rect.y -= Ball.Vel_y
            if (self.rect.x < 10):
                Ball.go_left = False
                Ball.go_right = True
                Ball.Vel_y = random.uniform(1.0, 2.0)
            if (self.rect.y < 10):
                Ball.go_up = False
                Ball.go_down = True
                Ball.Vel_y = random.uniform(1.0, 2.0)
        if Ball.Intersect(self.rect.x, x_platform, self.rect.y, y_platform, 20, 75):
            Ball.go_down = False
            Ball.go_up = True
            Ball.Vel_y = random.uniform(1.0, 2.0)
        Ball.collide(self, platforms)


