import pygame
from pygame.locals import *
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
number=["A0","A1","A2","A3","A4","B0","B1","B2","B3"]
icon=["mz.png","mz.png","mz.png","mz.png","kz.png","bz.png","bz.png","bz.png","bz.png"]
screen = pygame.display.set_mode((1240,768),0,32)#FULLSCREEN
screen.fill(Brack)
class Bottles(object):
    def Icon(num,x,y):
        img0=pygame.image.load(icon[num])
        screen.blit(img0,(x,y))
        text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",46)
        text_fmt0=text.render(number[num],3,White)
        screen.blit(text_fmt0,(x-80,y+50))
        pygame.display.update()
if __name__ == '__main__':
    Bottles.Icon(0,160,50)
    Bottles.Icon(1,530,50)
    Bottles.Icon(2,890,50)
    Bottles.Icon(3,160,290)
    Bottles.Icon(4,530,290)
    Bottles.Icon(5,890,290)
    Bottles.Icon(6,160,530)
    Bottles.Icon(7,530,530)
    Bottles.Icon(8,890,530)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            elif event.type == QUIT:
                exit()
