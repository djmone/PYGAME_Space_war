import pygame


BS_speed = 10

class Gun():
    
    def __init__(self, screen, stats): #Параметры Пушки
        
        self.screen = screen
        self.image = pygame.image.load('Image/BattelShip.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 480
        self.rect.bottom = 896-53*4
        self.MoveRight = False
        self.MoveLeft = False

    
        
    def output(self):
        self.screen.blit(self.image, self.rect)
    def update(self): #Движение Пушки
        if self.MoveRight and self.rect.right < self.screen_rect.right-170:
            self.rect.centerx += BS_speed
        if self.MoveLeft and self.rect.left > 165:
            self.rect.centerx -= BS_speed
        

