import pygame


class Bg():
    def __init__(self, screen):
    
        self.screen = screen
        self.image = pygame.image.load('Image/BG_image.png')
        self.image = pygame.transform.scale(self.image, (1024, 896))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    
        
    def output(self):
        self.screen.blit(self.image, self.rect)
