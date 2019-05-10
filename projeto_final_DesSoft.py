# -*- coding: utf-8 -*-
"""
Created on Fri May  3 08:09:07 2019

@author: Helio
"""
#Projeto final primeiro semestre de DesSoft
import pygame
import time
from os import path
import random

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
        player_img=pygame.image.load(path.join(img_dir,'bomb1.png')).convert()#colocar o nome da imagem do jogador
        self.image=player_img
        self.image=pygame.transform.scale(player_img,(15,14))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH)-15
        self.rect.bottom = (HEIGHT)-14
        self.speedx=0
        self.speedy=0
        self.radius=10
        '''self.shoot_delay= 500
        self.last_shoot= pygame.time.get_ticks()'''
        
    def update(self):
        '''keystate=pygame.key.get_pressed()'''
        self.rect.y+=self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
        if self.rect.top <0 :
            self.rect.top=0
        '''
        if keystate[pygame.K_SPACE]:
            self.shoot()'''
       
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img=pygame.image.load(path.join(img_dir,'bomb1.png')).convert()#colocar o nome da imagem do jogador
        self.image=player_img
        self.image=pygame.transform.scale(player_img,(15,14))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 0
        self.speedx=0
        self.speedy=0
        self.radius=10
        ''''self.shoot_delay= 500
        self.last_shoot= pygame.time.get_ticks()'''
        
    def update(self):
        '''keystate=pygame.key.get_pressed()'''
        self.rect.y+=self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
        if self.rect.top <0 :
            self.rect.top=0
        '''if keystate[pygame.K_SPACE]:
            self.shoot()'''
            
#cria os muros destruivel
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        mob_img = pygame.image.load(path.join(img_dir, "exp1.jpg")).convert()#Colocar imagem do muro
        self.image = pygame.transform.scale(mob_img, (50, 38))
        self.image.set_colorkey(BLACK)
        #---------------------------------------------------------------Arrumar
        self.rect = self.image.get_rect()
        # Sorteia um lugar inicial em x
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        '''
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)
        '''
        self.radius = int(self.rect.width * .85 / 2)#ajustar o tamanho dos mobs
    #atualiza a posição do jogador   
    '''
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy'''
        
class Bomb1(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        bomb_img = pygame.image.load(path.join(img_dir, "Bomb1.png")).convert()#colocar a imagem da bomba
        self.image=bomb_img
        self.image = bomb_img
        self.image=pygame.transform.scale(bomb_img,(15,14))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 0
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy 

#criando a explosãp da bomba


            
        
        
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Bomberman")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'campo.png')).convert()#colocar o mapa do jogo
background_rect = background.get_rect()

# Carrega os sons do jogo
'''pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))#colocar os sons
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))#arrumar som
destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))#arrumar som
pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))#arrumar som'''

# Cria uma nave. O construtor será chamado automaticamente.
player1 = Player1()
player2=Player2()

# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

# Cria um grupo só dos meteoros
mobs = pygame.sprite.Group()

# Cria um grupo para tiros
bombs = pygame.sprite.Group()

# Cria 8 meteoros e adiciona no grupo meteoros
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    '''
    pygame.mixer.music.play(loops=-1)'''
    running = True
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
                    player1.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player1.speedx = 8
                if event.key==pygame.K_UP:
                    player1.speedy=- 8
                if event.key==pygame.K_DOWN:
                    player1.speedy=8
                if event.key==pygame.K_w:
                    player2.speedy=-8
                if event.key==pygame.K_s:
                    player2.speedy=8
                if event.key==pygame.K_a:
                    player2.speedx=-8
                if event.key==pygame.K_d:
                    player2.speedx=8
                
                        
                # Se for um espaço atira!
                if event.key == pygame.K_SPACE:
                    bomb = Bomb1(player1.rect.centerx, player1.rect.top)
                    all_sprites.add(bomb)
                    bombs.add(bomb)
                    '''
                    pew_sound.play()'''
                if event.key == pygame.K_e:
                    bomb = Bomb1(player2.rect.centerx, player2.rect.top)
                    all_sprites.add(bomb)
                    bombs.add(bomb)
                    '''
                    pew_sound.play()'''
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player1.speedx = 0
                if event.key==pygame.K_DOWN:  
                    player1.speedy=0
                if event.key == pygame.K_RIGHT:
                    player1.speedx = 0
                if event.key==pygame.K_UP:   
                    player1.speedy=0
                if event.key==pygame.K_w:
                    player2.speedy=0
                if event.key==pygame.K_s:
                    player2.speedy=0
                if event.key==pygame.K_a:
                    player2.speedx=0
                if event.key==pygame.K_d:
                    player2.speedx=0
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        # Verifica se houve colisão entre tiro e meteoro
        hits = pygame.sprite.groupcollide(mobs, bombs, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            '''
            destroy_sound.play()'''
            m = Mob() 
            all_sprites.add(m)
            mobs.add(m)
        
        # Verifica se houve colisão entre nave e meteoro
        hits = pygame.sprite.spritecollide(player1, mobs, False, pygame.sprite.collide_circle)
        hits = pygame.sprite.spritecollide(player2, mobs, False, pygame.sprite.collide_circle)
        if hits:
            # Toca o som da colisão
            '''
            boom_sound.play()'''
            time.sleep(1) # Precisa esperar senão fecha
            
            running = False
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    
    pygame.quit()

           