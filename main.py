import pygame
from sys import exit

from player import Player
import obstacles

pygame.init()
screen = pygame.display.set_mode((1300,400))
pygame.display.set_caption('sideways game')
clock = pygame.time.Clock()

player_1 = Player(screen)
#delete move var
while True:
    move = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                move = True

    screen.fill("#23480a")
    player_1.update()
    obstacles.create_rect()
    for i in obstacles.obstacles:
        i.update(screen)
        if move == True:
            if i.remove():
                obstacles.obstacles.remove(i)
                print("a")
            i.rect.x -= 100
            

    pygame.display.update()
    clock.tick(60)

