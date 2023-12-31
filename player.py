import pygame
from obstacles import obstacles

class Player:
    def __init__(self,screen):
        self.rect = pygame.Rect(0,0,40,80)
        self.x_speed = 0
        self.screen = screen
        self.gravity = 0
        self.jumping = False
        self.grounded = False
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_speed -=1
        if keys[pygame.K_d]:
            self.x_speed +=1
        #jump
        if keys[pygame.K_SPACE] and self.grounded:
            self.gravity = -22
        
    def movement(self):
        #left and right
        self.rect.x += self.x_speed
        if self.x_speed > 0:self.x_speed -=0.5
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

        #grounded
        if self.rect.bottom >= 395:
            self.grounded = True
    
    def colision_side_check(self, rect):
        delta_x = rect.centerx - self.rect.centerx
        delta_y = rect.centery - self.rect.centery

        abs_delta_x = abs(delta_x)
        abs_delta_y = abs(delta_y)

        if abs(abs_delta_x - abs_delta_y) < 25:
            return

        if abs_delta_x > abs_delta_y:
            if delta_x > 0:
                return "right"
            else:
                return "left"
        else:
            if delta_y > 0 :
                if self.gravity > 0:
                    return "bottom"
            else:
                return "top"
            
    def colisions(self, rect):
        if rect.colliderect(self.rect):
            collision_side = self.colision_side_check(rect)

            if collision_side == "bottom":
                self.rect.bottom = rect.top
                self.gravity = 0
                self.grounded = True       
            if collision_side == "top":
                self.rect.top = rect.bottom
                self.gravity = 0
            if collision_side == "left":
                self.rect.left = rect.right
                self.x_speed = 0
            if collision_side == "right":
                self.rect.right = rect.left
                self.x_speed = 0

    def draw(self):
        pygame.draw.rect(self.screen, ('#0a2348'), self.rect)
    
    def update(self):
        self.input()
        self.movement()
        self.grounded = False
        self.screen_side_check()
        for i in obstacles:
            self.colisions(i.rect)
        self.draw()