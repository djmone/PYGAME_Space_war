import pygame, GameController
from pygame.sprite import Group
import time
import sys
import os



from pygame.time import Clock
from GunLogic import Gun
from Bg import Bg
from bullet import Bullet
from AlienLogic  import Alien
from MyStatistic import Statistic
from Raiting import Score






def run():

    pygame.init()
    pygame.mixer.music.load('Sound/BGSound.mp3')
    pygame.mixer.music.set_volume(0.07)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((1024, 896))
    pygame.display.set_caption("Space Invaders v0.1")
    bg_image = pygame.image.load('Image/BG_image.png')
    
    Shot_Sound = pygame.mixer.Sound('Sound/Shot.wav')
    Shot_Sound.set_volume(0.05)

    ShipDeadSound = pygame.mixer.Sound('Sound/ShipDead.wav')
    ShipDeadSound.set_volume(0.05)

    GOSound = pygame.mixer.Sound('Sound/GameOver.mp3')
    GOSound.set_volume(0.05)

    stats = Statistic()
    gun = Gun(screen, stats)
    bg = Bg(screen)
    bullets = Group()
    aliens = Group()
    GameController.create_aliens(screen, aliens)
    stats = Statistic()
    speedAli = 1
    sc = Score(screen, stats, speedAli)
    Timer = 0

    

    FPS=30
    clock = pygame.time.Clock()
    NotLose = 1

    while True:
        GameController.events(screen, gun, bullets, stats, Shot_Sound)
        bg.output() #��������� ����
        sc.draw_score()
        for bullet in bullets.sprites(): #���������� ������� ����
            bullet.update()    
        for bullet in bullets.sprites(): #��������� ���� ����
            bullet.draw()
        for alienShip in aliens.sprites():
            if alienShip.rect.y>=610:
                if stats.gun_live>0:
                    stats.gun_live -=1
                    sc.image_now_HP()
                    GameController.res(stats, screen, gun,aliens, bullets)

                    break
                if stats.gun_live==0:
                    print("You lose")
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(GOSound)
                    aliens.empty()
                    NotLose = 0
                    
                    break
        if len(aliens)==0 and stats.gun_live>=0 and NotLose==1:
            speedAli +=1
            sc.Your_LVL(speedAli)
            GameController.res(stats, screen, gun,aliens, bullets)
        gun.update() #���������� ������� ������� ������
        if NotLose == 0:
            stats.StopB = True
            bullets.empty()
            sc.You_Lose()
            sc.draw_lose()
            

        if NotLose ==0:
            Timer +=1/FPS
            if Timer >=2:
                stats.res = True
        if stats.GoRes:
            run()
        gun.output() #��������� ������� ������
        aliens.draw(screen) #��������� ����������
        GameController.bullets_cheker(aliens,stats, sc, bullets, speedAli, ShipDeadSound) #������ ������ ��� �������� ����������� ����������
        aliens.update(aliens, speedAli) #���������� ������� ����������
        
        
        pygame.display.flip() #������ �����������

        clock.tick(FPS) #����� �� pygame ��� ������������ ������� ������

run()