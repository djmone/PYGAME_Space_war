import pygame, sys
from bullet import Bullet
from AlienLogic  import Alien
from MyStatistic import Statistic
import time





def events(screen, gun, bullets,stats,Shot_Sound,sc):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and not(stats.StopB):
                gun.MoveRight = True
            if event.key == pygame.K_a and not(stats.StopB):
                gun.MoveLeft = True
            if event.key == pygame.K_r and stats.res:
                stats.GoRes = True
            if event.key == pygame.K_ESCAPE:
                pause(sc)
            
            if event.key == pygame.K_SPACE and not(stats.StopB):
                if len(bullets)<=2: #2
                    pygame.mixer.Sound.play(Shot_Sound)
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.MoveRight = False
            if event.key == pygame.K_a:
                gun.MoveLeft = False
                

def bullets_cheker(aliens, stats, sc, bullets, speedAli, ShipDeadSound):
    for bullet in bullets.copy():
        if bullet.rect.bottom <=172:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            pygame.mixer.Sound.play(ShipDeadSound)
            stats.score +=10 * len(aliens) * speedAli
        sc.image_now_score()
        Ckeck_HScore(stats, sc)


def res(statistic, screen, gun, aliens, bullets):

    print(statistic.gun_live)
    bullets.empty()
    aliens.empty()
    create_aliens(screen, aliens)

def create_aliens(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    SUM_aliens = 9
    row=5
    for row in range(row):
        for alien_n in range (SUM_aliens):
            alien = Alien(screen)
            alien.x = alien_width + ((alien_width+20) * alien_n) + 130
            alien.y = alien_height + ((alien_height+20) * row) +130
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien)


def Ckeck_HScore (stats, sc):
    if stats.score > stats.HScore:
        stats.HScore = stats.score
        sc.image_now_HScore()
        with open ('HS.txt', 'w') as f:
            f.write(str(stats.HScore))

    
def pause(sc):
    paused = True
    while paused:
        sc.pouse_text()
        sc.draw_pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
        pygame.display.update()
        time.sleep(0.1)

    


    
