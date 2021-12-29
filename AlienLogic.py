import pygame
import time
from MyStatistic import Statistic
from Raiting import Score

class Alien(pygame.sprite.Sprite):

    def __init__(self, screen ): #Параметры Инопланетянина
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('Image/ship 1-1.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.AnimatorTime = 0
        self.start_time = time.time
        self.AnimatorChecker = False
        self.RLposition=0
        self.Right = True
        self.speed = 1
        


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, aliens, speedAli):

        if len(aliens)==45:
            self.speed = speedAli

        if len(aliens)==40:
            self.speed = speedAli + 0.2

        if len(aliens)==35:
            self.speed = speedAli + 0.4

        if len(aliens)==30:
            self.speed = speedAli + 0.6

        if len(aliens)==25:
            self.speed = speedAli + 0.8

        if len(aliens)==20:
            self.speed = speedAli + 1

        if len(aliens)==20:
            self.speed = speedAli + 1.2

        if len(aliens)==15:
            self.speed = speedAli + 1.4

        if len(aliens)==10:
            self.speed = speedAli + 1.6

        if len(aliens)==5:
            self.speed = speedAli + 1.8


        ###Движение влево, вправо и вниз###
        if self.Right:
            self.x += self.speed
            self.RLposition += self.speed
            self.rect.x = self.x
            if self.RLposition >=150:
                self.Right = False
                self.y +=20
                self.RLposition=0 
        if self.Right==False:
            self.x -= self.speed
            self.RLposition += self.speed
            self.rect.x = self.x
            if self.RLposition >=150:
                self.Right = True
                self.y +=20
                self.RLposition=0
        ###Анимация кораблей###
        self.AnimatorTime+=1
        self.rect.y = self.y
        if self.AnimatorTime >=20 and self.AnimatorChecker == False:
            self.image = pygame.image.load('Image/ship 1-2.png')
            self.image = pygame.transform.scale(self.image,(self.image.get_width() * 2, self.image.get_height() * 2))
            self.AnimatorTime = 0
            self.AnimatorChecker = True
        if self.AnimatorTime >=20 and self.AnimatorChecker == True:
            self.image = pygame.image.load('Image/ship 1-1.png')
            self.image = pygame.transform.scale(self.image,(self.image.get_width() * 2, self.image.get_height() * 2))
            self.AnimatorTime = 0
            self.AnimatorChecker = False
