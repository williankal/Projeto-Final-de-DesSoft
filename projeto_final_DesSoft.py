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
#cria os muros destruivel
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        mob_img = pygame.image.load(path.join(img_dir, ".png")).convert()#Colocar imagem do muro
        self.image = pygame.transform.scale(mob_img, (50, 38))
        self.image.set_colorkey(BLACK)
"""       Arrumar
        # Sorteia um lugar inicial em x
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)
        self.radius = int(self.rect.width * .85 / 2)#ajustar o tamanho dos mobs"""
    #atualiza a posição do jogador   
     def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
class Bomb(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        bomb_img = pygame.image.load(path.join(img_dir, "")).convert()#colocar a imagem da bomba
        self.image = bomb_img
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = position1
        self.rect.centerx = x
        self.speedy = -10
        

           