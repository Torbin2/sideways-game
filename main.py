import pygame
from sys import exit

from player import Player


pygame.init()
screen = pygame.display.set_mode((1300,400))
pygame.display.set_caption('sideways game')
clock = pygame.time.Clock()

player_1 = Player(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    screen.fill("green")
    player_1.update()

    pygame.display.update()
    clock.tick(60)

