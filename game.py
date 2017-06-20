# -*- coding:utf-8- -*-

import pygame
from platforms import Platform
from ball import Ball
from arcanoid import Arcanoid

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('A R C A N O I D v1.0')
screen = pygame.Surface((400, 400))
timer = pygame.time.Clock()


left=right=False
ball = Ball(250, 250)
arcanoid = Arcanoid(250, 350)

level = [
    '----------',
    ' -------- ',
    '  ------  ',
    '   ----   ',
    '    --    ']

sprite_group = pygame.sprite.Group()
sprite_group.add(ball)
sprite_group.add(arcanoid)
platf = []

x = 25
y = 25
for row in level:
    for col in row:
        if col == '-':
            pl = Platform (x, y)
            sprite_group.add(pl)
            platf.append(pl)
        x += 35
    y += 40
    x = 25

done = True
pygame.key.set_repeat(1, 1)

while done:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type ==pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left=True
                right=False
            if e.key == pygame.K_RIGHT:
                right=True
                left=False
        arcanoid.update(left, right)

    screen.fill((50, 50, 50))
    ball.update(arcanoid.rect.x, arcanoid.rect.y, platf)
    sprite_group.draw(screen)
    window.blit(screen, (0, 0))
    pygame.display.flip()
    timer.tick(60)#cdvdcfbf