# -*- coding: utf-8 -*-
"""
Created on Fri May  3 08:09:07 2019

@author: Helio
"""
#Projeto final primeiro semestre de DesSoft
import pygame
import time
from os import path

#estabelecendo a pasta com as figuras e sons
img_dir=path.join(path.dirname(__file__),'img')
snd_dir=path.join(path.dirname(__file__),'snd')

#definindo o tamanho da tela
WIDTH=600
HEIGHT=480
FPS=60 

#definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#criando o player 1
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img=pygame.image.load(path.join(img_dir,'#nomedaimagem')).convert()#colocar o nome da imagem do jogador
        self.image=player_img
        self.img=pygame.transform.scale((player_img(15,14)))
        self.image.setcolorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = max(WIDTH)
        self.rect.bottom = max(HEIGHT)
        self.speedx=10
        self.radius=10
        
    def position1(self):
       self.rect.x += self.speedx
       if self.rect.right > WIDTH:
           self.rect.right = WIDTH
       if self.rect.left < 0:
           self.rect.left = 0
           
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img=pygame.image.load(path.join(img_dir,'#nomedaimagem')).convert()#colocar o nome da imagem do jogador
        self.image=player_img
        self.img=pygame.transform.scale((player_img(15,14)))
        self.image.setcolorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = min(WIDTH)
        self.rect.bottom = min(HEIGHT)
        self.speedx=10
        self.radius=10
        
    def position2(self):
       self.rect.x += self.speedx
       if self.rect.right > WIDTH:
           self.rect.right = WIDTH
       if self.rect.left < 0:
           self.rect.left = 0
#cria os muros destruiveis
           