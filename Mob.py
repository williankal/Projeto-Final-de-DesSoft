import pygame
import random
from config import *

class Mob(pygame.sprite.Sprite):
    def __init__(self, size, fire_anim):
        pygame.sprite.Sprite.__init__(self)
        self.fire_anim = fire_anim
        self.size=size
        self.image=self.fire_anim[self.size][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.last_update=pygame.time.get_ticks()
        self.frame=0
        self.frame_rate=100
        
       
        self.rect = self.image.get_rect()
        # Sorteia um lugar inicial em x
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)
        
        self.radius = int(self.rect.width * .85 / 2)#ajustar o tamanho dos fogos
    #atualiza a posição do jogador   
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #se o fogo passar da tela volta para cima
        if self.rect.top>HEIGHT+10 or self.rect.left<-25 or self.rect.right>WIDTH+20:
            self.rect.x=random.randrange(WIDTH - self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedx=random.randrange(-3,3)
            self.speedy=random.randrange(2,9)
        now=pygame.time.get_ticks()
        if now - self.last_update>self.frame_rate:
            self.last_update= now
            self.frame +=1
            if self.frame==len(self.fire_anim[self.size]):
                self.frame=0

            center= self.rect.center
            self.image=self.fire_anim[self.size][self.frame]
            self.rect= self.image.get_rect()
            self.rect.center= center