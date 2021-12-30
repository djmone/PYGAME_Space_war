
import pygame




class Button:
    def __init__(self, width, height,screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactiv_color = (23,204,58)
        self.activ_color = (13,162,58)
        self.fontType = pygame.font.SysFont(None, 130)
        self.fontColor = (255,255,255)
        self.GameStarted = False
        self.GameNotQuit = True

    def drawButton(self, x, y, message,BTSound, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x+self.width and y<mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.inactiv_color, (x,y, self.width,self.height))
            if click[0] ==1:
                print('hi')
                self.GameStarted = True
                pygame.mixer.Sound.play(BTSound)
                pygame.time.delay(300)
                if action is not None:
                    if action == quit:
                        self.GameNotQuit= False
                    
        else:
            pygame.draw.rect(self.screen, self.activ_color, (x,y, self.width,self.height))

        
        
        self.text = self.fontType.render(message, True, self.fontColor)
        self.screen.blit(self.text, (x+90,y+10))
