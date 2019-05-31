import pygame
import random
from os import path
import numpy as np

from config import img_dir, WHITE, BLACK , FPS, GAME, QUIT


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'inicio.png')).convert()
    background=pygame.transform.scale(background,(480,600))
    background_rect = background.get_rect()

    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
                    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(WHITE)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

class final_explosion1(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=final_exp1[self.size][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
        
     
    def update(self):
        '''keystate=pygame.key.get_pressed()'''
        now=pygame.time.get_ticks()
        if now - self.last_update>self.frame_rate:
            self.last_update= now
            self.frame +=1
            if self.frame==len(final_exp1[self.size]):
                self.frame=0

            center= self.rect.center
            self.image=final_exp1[self.size][self.frame]
            self.rect= self.image.get_rect()
            self.rect.center= center
            

class final_explosion2(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=final_exp2[self.size][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
        
     
    def update(self):
        '''keystate=pygame.key.get_pressed()'''
        now=pygame.time.get_ticks()
        if now - self.last_update>self.frame_rate:
            self.last_update= now
            self.frame +=1
            if self.frame==len(final_exp2[self.size]):
                self.frame=0

            center= self.rect.center
            self.image=final_exp2[self.size][self.frame]
            self.rect= self.image.get_rect()
            self.rect.center= center
            
#criando a animacao da tela final
final_exp1={}
final_exp1['f1']=[]
for a in np.arange(1,7,1):
    filename='finalexp{0}.png'.format(a)
    img=pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img, (480,600))
    final_exp1['f1'].append(img_lg)

final_exp2={}
final_exp2['f2']=[]
for a in np.arange(1,7,1):
    filename='final2exp{0}.png'.format(a)
    img=pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img, (480,600))
    final_exp2['f2'].append(img_lg)

all_sprites = pygame.sprite.Group()                
finalexp1=final_explosion1('f1')
all_sprites.add(finalexp1)
finalexp2=final_explosion2('f2')
all_sprites.add(finalexp2)

def final_screen(screen,hits1,hits2):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    

    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        if hits1:
            final_explosion2('f2')
            state = QUIT
            running = False

        if hits2:
            final_explosion1('f1')
            state = GAME
            running = False
                    
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state