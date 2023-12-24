import pygame

class Player:
    def __init__(self,screen):
        self.rect = pygame.Rect(0,0,40,80)
        self.x_speed = 0
        self.screen = screen
        self.gravity = 0
        self.jumping = False
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_speed -=1
        if keys[pygame.K_d]:
            self.x_speed +=1
        #jump
        if keys[pygame.K_SPACE] and self.rect.bottom >= 390:
            self.gravity = -22
        
    def movement(self):
        #left and right
        self.rect.x += self.x_speed
        if self.x_speed >= 0:self.x_speed -=0.5
        if self.x_speed < 0:self.x_speed +=0.5  

        #gravity
        self.gravity += 1
        self.rect.centery += self.gravity


    def screen_side_check(self):
        #side of the screen colisions
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
        if self.rect.top <= -1:
            self.rect.top = 0

        if self.rect.right >= 1300: 
            self.rect.right = 1300
            self.x_speed -= 2
        if self.rect.left <= 0: 
            self.rect.left = 0
            self.x_speed += 2
    


    def draw(self):
        pygame.draw.rect(self.screen, ('#18232d'), self.rect)
    
    def update(self):
        self.input()
        self.movement()
        self.screen_side_check()
        self.draw()