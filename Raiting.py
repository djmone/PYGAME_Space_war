from sys import float_info
import pygame.font


class Score():
    
    def __init__(self, screen, stats, speedAli):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 26)
        self.fontLose = pygame.font.SysFont(None, 56)
        self.image_now_score()
        self.image_now_HScore()
        self.imgage_HS_img()
        self.imgage_HP_img()
        self.image_now_HP()
        self.Your_LVL(speedAli)
        self.You_Lose()


    def image_now_score(self):
        self.score_im = self.font.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.score_rect = self.score_im.get_rect()
        self.score_rect.right = self.screen_rect.right - 300
        self.score_rect.top = 145



    def image_now_HScore(self):
        self.HS_image = self.font.render(str(self.stats.HScore), True, self.text_color, (0,0,0))
        self.HS_rect = self.HS_image.get_rect()
        self.HS_rect.right = self.screen_rect.right - 400
        self.HS_rect.top = 145

    def imgage_HS_img(self):
        self.imageHS = pygame.image.load('Image/HiScore.png')
        self.imageHS_rect = self.imageHS.get_rect()
        self.imageHS_rect.right = self.screen_rect.right - 470
        self.imageHS_rect.top = 145

    def imgage_HP_img(self):
        self.imageHP = pygame.image.load('Image/HP.png')
        self.imageHP_rect = self.imageHP.get_rect()
        self.imageHP_rect.right = self.screen_rect.right - 650
        self.imageHP_rect.top = 146

    def image_now_HP(self):
        self.HP_image = self.font.render(str(self.stats.gun_live), True, self.text_color, (0,0,0))
        self.HP_rect = self.HP_image.get_rect()
        self.HP_rect.right = self.screen_rect.right - 630
        self.HP_rect.top = 145

    def Your_LVL(self, speedAli):
        self.LVL_image = self.font.render('LVL:' , True, self.text_color, (0,0,0))
        self.LVL_rect = self.LVL_image.get_rect()
        self.LVL_rect.right = self.screen_rect.right - 800
        self.LVL_rect.top = 145

        self.LVLN_image = self.font.render(str(speedAli) , True, self.text_color, (0,0,0))
        self.LVLN_rect = self.LVLN_image.get_rect()
        self.LVLN_rect.right = self.screen_rect.right - 790
        self.LVLN_rect.top = 145

    def You_Lose(self):
        self.LoseR_image = self.fontLose.render('PRESS (R) TO RESTART' , True, self.text_color, (0,0,0))
        self.LoseR_rect = self.LoseR_image.get_rect()
        self.LoseR_rect.centerx = self.screen_rect.centerx
        self.LoseR_rect.top = 200
        
        self.Lose_image = self.fontLose.render('YOU LOSE!!! YOUR SCORE:' , True, self.text_color, (0,0,0))
        self.Lose_rect = self.Lose_image.get_rect()
        self.Lose_rect.centerx = self.screen_rect.centerx
        self.Lose_rect.top = 300

        self.LoseS_im = self.fontLose.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.LoseS_rect = self.LoseS_im.get_rect()
        self.LoseS_rect.centerx = self.screen_rect.centerx
        self.LoseS_rect.top = 356

    def draw_score(self):
        self.screen.blit(self.score_im, self.score_rect)
        self.screen.blit(self.HS_image, self.HS_rect)
        self.screen.blit(self.imageHS, self.imageHS_rect)
        self.screen.blit(self.imageHP, self.imageHP_rect)
        self.screen.blit(self.HP_image, self.HP_rect)
        self.screen.blit(self.LVL_image, self.LVL_rect)
        self.screen.blit(self.LVLN_image, self.LVLN_rect)
        
        
    def draw_lose(self):
        self.screen.blit(self.Lose_image, self.Lose_rect)
        self.screen.blit(self.LoseS_im, self.LoseS_rect)
        self.screen.blit(self.LoseR_image, self.LoseR_rect)
        