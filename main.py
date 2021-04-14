# -*- coding: utf-8 -*-
"""
Created on Fri May  3 08:09:07 2019

@author: Helio
"""
#pygamecolidemask
#Projeto final primeiro semestre de DesSoft
import pygame

import time
from os import path
import random
import numpy as np
from init_screen import init_screen, final_screen
from config import *

from Player import Player
from Mob import Mob
from Explosion import Explosion
from Bomb import Bomb
from Wall import Wall

pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#estabelecendo a pasta com as figuras e sons
img_dir = path.join(path.dirname(__file__),'img')
snd_dir = path.join(path.dirname(__file__),'snd')

# Inicialização do Pygame.    

# Nome do jogo
pygame.display.set_caption("InsperBomb")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()


# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'hellfundo.png')).convert()#colocar o mapa do jogo
background = pygame.transform.scale(background, (WIDTH,HEIGHT))#transforma a escala do png
background_rect = background.get_rect()

#Música
#pygame.mixer.music.load(path.join(snd_dir, 'theme.mp3'))
pygame.mixer.music.set_volume(0.8)
boom_sound = pygame.mixer.Sound(path.join(snd_dir,'explio.wav'))
death_sound = pygame.mixer.Sound(path.join(snd_dir,'death.wav'))

#animação do jogador1
player1_anim = {}
player1_anim['front'] = []
for a in np.arange(1,3,1):
    filename = 'pl1_front{0}.png'.format(a)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (40,40))
    player1_anim['front'].append(img_lg)
  
#carrega animação jogador 2
player2_anim = {}
player2_anim['front2'] = []
for a in np.arange(1,3,1):
    filename ='pl2_front{0}.png'.format(a)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (40,40))
    player2_anim['front2'].append(img_lg)

#animacão do fogo
fire_anim = {}
fire_anim['fire'] = []
for a in np.arange(1,3,1):
    filename = 'fire_anim{0}.png'.format(a)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (50,50))
    fire_anim['fire'].append(img_lg)

#carrega a imagem das explosões
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in np.arange(1,14,1):
    filename = 'Explosion-{0}.png.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (120,120))
    explosion_anim['lg'].append(img_lg)
    

# Carrega os sons do jogo
'''pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))#colocar os sons
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))#arrumar som
destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))#arrumar som
pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))#arrumar som'''

# Cria um jogador. O construtor será chamado automaticamente
player1 = Player('front', player1_anim, (WIDTH,HEIGHT))
player2 = Player('front2', player2_anim, (0,0))

# Cria um grupo de todos os sprites e adiciona ao player.
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

#cria um grupo para as explosões
exp = pygame.sprite.Group()

#Cria um grupo só dos meteoros
mobs = pygame.sprite.Group()

# Posição das paredes no mapa
bombPlayer1 = pygame.sprite.Group()
bombPlayer2 = pygame.sprite.Group()
bombs = pygame.sprite.Group()
walls = pygame.sprite.Group()

x = (WIDTH-(4*WALL_WIDTH))/5
y = (HEIGHT-(4*WALL_HEIGHT))/5

for i in range(1,5):
    for j in range(1,5):
        m = Wall(x*j+WALL_WIDTH*(j-1), y*i+WALL_HEIGHT*(i-1))
        all_sprites.add(m)
        walls.add(m)
        
# Cria 8 meteoros e adiciona no grupo meteoros
for i in range(1):
    m = Mob('fire', fire_anim)
    all_sprites.add(m)
    mobs.add(m)
 
# Comando para evitar travamentos.
try:
    
    # Loop principal.
    #pygame.mixer.music.play(loops=-1)
    running = True
    init_screen(screen)
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player1.move('left')
                if event.key == pygame.K_RIGHT:
                    player1.move('right')
                if event.key == pygame.K_UP:
                    player1.move('up')
                if event.key == pygame.K_DOWN:
                    player1.move('down')

                if event.key == pygame.K_a:
                    player2.move('left')
                if event.key == pygame.K_d:
                    player2.move('right')
                if event.key == pygame.K_w:
                    player2.move('up')
                if event.key == pygame.K_s:
                    player2.move('down')
                
                # Se for um espaço atira!
                if event.key == pygame.K_SPACE:
                    player1.plant_bomb(all_sprites, bombPlayer1)

                if event.key == pygame.K_e :
                    player2.plant_bomb(all_sprites, bombPlayer2)

            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player1.stop('x')
                if event.key == pygame.K_RIGHT:
                    player1.stop('x')
                if event.key == pygame.K_UP:   
                    player1.stop('y')
                if event.key == pygame.K_DOWN:  
                    player1.stop('y')

                if event.key == pygame.K_a:
                    player2.stop('x')
                if event.key == pygame.K_d:
                    player2.stop('x')   
                if event.key == pygame.K_w:
                    player2.stop('y')
                if event.key == pygame.K_s:
                    player2.stop('y')
                    
        # Jogodores colidem com as paredes
        for wall_collider in pygame.sprite.spritecollide(player1, walls, False):
            player1.avoid_collision(wall_collider)

        for wall_collider in pygame.sprite.spritecollide(player2, walls, False):
            player2.avoid_collision(wall_collider)

        # Jogadores colidem com as bombas
        for bomb_collider in pygame.sprite.spritecollide(player1, bombPlayer2, False):
            player1.avoid_collision(bomb_collider)
       
        for bomb_collider in pygame.sprite.spritecollide(player2, bombPlayer1, False):
            player2.avoid_collision(bomb_collider)
            
        # Depois de processar os eventos.
        # Atualiza a ação de cada sprite.
        all_sprites.update()
                
        # # Verifica se houve colisão entre tiro e meteoro
        hits = pygame.sprite.groupcollide(mobs, bombPlayer1, True, True)
        hits3 = pygame.sprite.groupcollide(mobs, bombPlayer2, True, True)

        for hit in hits:             
            boom_sound.play()
            expl = Explosion(hit.rect.center, 'lg', explosion_anim)
            exp.add(expl)
            all_sprites.add(expl)
            m = Mob('fire', fire_anim) 
            all_sprites.add(m)
            mobs.add(m)
        
        for hit in hits3:             
            boom_sound.play()
            expl = Explosion(hit.rect.center, 'lg', explosion_anim)
            exp.add(expl)
            all_sprites.add(expl)
            m = Mob('fire', fire_anim) 
            all_sprites.add(m)
            mobs.add(m)

        hits1 = pygame.sprite.spritecollide(player1, exp, False, pygame.sprite.collide_circle)
        hits2 = pygame.sprite.spritecollide(player2, exp, False, pygame.sprite.collide_circle)
        #     # Toca o som da colisão
        #     death_sound.play()
        #     time.sleep(1)
        #     '''
        #     boom_sound.play()'''
        #     running=False
        #     # Precisa esperar se não fecha
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        
        # Depois de desenhar tudo, inverte o display.
        
        pygame.display.flip()
        
    final_screen(screen,hits1,hits2)  
    time.sleep(3)     
finally:
    
    pygame.quit()

           