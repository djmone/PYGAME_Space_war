import pygame, GameController
from pygame import display
from pygame.sprite import Group
import time
import pygame.font



from pygame.time import Clock
from GunLogic import Gun
from Bg import Bg
from bullet import Bullet
from AlienLogic  import Alien
from MyStatistic import Statistic
from Raiting import Score
from ButtonLogic import Button

screen = pygame.display.set_mode((1024, 896))
clock = pygame.time.Clock()

ItsRes = True
def run():
    global ItsRes
    pygame.init()
    pygame.mixer.music.load('Sound/BGSound.mp3')
    pygame.mixer.music.set_volume(0.01) #0.07
    pygame.mixer.music.play(-1)

    BTSound = pygame.mixer.Sound('Sound/BTSound.mp3')
    BTSound.set_volume(0.05)
    
    pygame.display.set_caption("Space Invaders v0.1")

    bg_image = pygame.image.load('Image/BG_image.png')
    
    
    Shot_Sound = pygame.mixer.Sound('Sound/Shot.wav')
    Shot_Sound.set_volume(0.05)

    ShipDeadSound = pygame.mixer.Sound('Sound/ShipDead.wav')
    ShipDeadSound.set_volume(0.05)
    menu_BG = pygame.image.load('Image/BG_menu.jpg')
    menu_BG = pygame.transform.scale(menu_BG,(menu_BG.get_width() * 1, menu_BG.get_height() * 1.05))

    

    GOSound = pygame.mixer.Sound('Sound/GameOver.mp3')
    GOSound.set_volume(0.05)

    stats = Statistic()
    gun = Gun(screen, stats)
    bg = Bg(screen)
    button = Button(400,100,screen)
    bullets = Group()
    aliens = Group()
    GameController.create_aliens(screen, aliens)
    stats = Statistic()
    speedAli = 10
    sc = Score(screen, stats, speedAli)
    Timer = 0


    FPS=30
    
    NotLose = 1

    while button.GameNotQuit and ItsRes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(menu_BG,(-250,0))
        button.drawButton(312,200,"Start", BTSound)
        button.drawButton(312,400,"Quit", BTSound, quit)
        Started = button.GameStarted
        if Started:
            break
        pygame.display.flip()
        clock.tick(FPS)


    while button.GameNotQuit:
        GameController.events(screen, gun, bullets, stats, Shot_Sound,sc)
        bg.output() #Отрисовка Фона
        sc.draw_score()
        for bullet in bullets.sprites(): #Обнволение позиций пуль
            bullet.update()    
        for bullet in bullets.sprites(): #Отрисоква всех пуль
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
        gun.update() #Обнволение позиций коробля игрока
        if NotLose == 0:
            stats.StopB = True
            bullets.empty()
            sc.You_Lose()
            sc.draw_lose()
            

        if NotLose ==0:
            Timer +=1/FPS
            if Timer >=2:
                stats.res = True
                
        if stats.GoRes and button.GameNotQuit:
            ItsRes= False
            run()
        gun.output() #Отрисовка коробля игрока
        aliens.draw(screen) #Отрисовка противника
        GameController.bullets_cheker(aliens,stats, sc, bullets, speedAli, ShipDeadSound) #Запуск метода для проверки уничтожения противника
        aliens.update(aliens, speedAli) #Обнволение позиций противника
        
        
        pygame.display.flip() #Двойна буфиризация

        clock.tick(FPS) #метод из pygame для фиксированой частоты кадров


run()



