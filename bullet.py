import pygame

class Bullet(pygame.sprite.Sprite): #Параметры пуль
    def __init__(self, screen, gun):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('Image/AmmoBattelShip.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width() * 1, self.image.get_height() * 1))
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
    def update(self):

        self.y -=self.speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
