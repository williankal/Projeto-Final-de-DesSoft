# -*- coding: utf-8 -*-
"""
Created on Fri May  3 08:09:07 2019

@author: Helio
"""
#pygamecolidemask
#Projeto final primeiro semestre de DesSoft
import pygame
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((480, 600))
import time
from os import path
import random
import numpy as np
from init_screen import init_screen, final_screen
from config import WIDTH, HEIGHT, INIT, GAME, QUIT


#estabelecendo a pasta com as figuras e sons
img_dir=path.join(path.dirname(__file__),'img')
snd_dir=path.join(path.dirname(__file__),'snd')

FPS=60 

#definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Classe do player 1
class Player1(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=player1_anim[self.size][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH)-15
        self.rect.bottom = (HEIGHT)-14
        self.speedx=0
        self.speedy=0
        self.radius=10
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
        self.pontos=3
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
        now=pygame.time.get_ticks()
        if now - self.last_update>self.frame_rate:
            self.last_update= now
            self.frame +=1
            if self.frame==len(player1_anim[self.size]):
                self.frame=0

            center= self.rect.center
            self.image=player1_anim[self.size][self.frame]
            self.rect= self.image.get_rect()
            self.rect.center= center
        '''
        if keystate[pygame.K_SPACE]:
            self.shoot()'''
#classe do player 2
class Player2(pygame.sprite.Sprite):
   def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=player2_anim[self.size][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH)
        self.rect.bottom = (HEIGHT)
        self.speedx=0
        self.speedy=0
        self.radius=10
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
        self.pontos=3
     
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
        now=pygame.time.get_ticks()
        if now - self.last_update>self.frame_rate:
            self.last_update= now
            self.frame +=1
            if self.frame==len(player2_anim[self.size]):
                self.frame=0

            center= self.rect.center
            self.image=player2_anim[self.size][self.frame]
            self.rect= self.image.get_rect()
            self.rect.center= center

#cria a class explosions 
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=explosion_anim[self.size][1]
        self.rect=self.image.get_rect()
        self.rect.center= center
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
        
    def update(self):
        now=pygame.time.get_ticks()
        if now - self.last_update>self.frame_rate:
            self.last_update= now
            self.frame +=1
            if self.frame==len(explosion_anim[self.size]):
                self.kill()
            else:
                center= self.rect.center
                self.image=explosion_anim[self.size][self.frame]
                self.rect= self.image.get_rect()
                self.rect.center= center
            
#cria os fogos
class Mob(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=fire_anim[self.size][1]
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
            if self.frame==len(fire_anim[self.size]):
                self.frame=0

            center= self.rect.center
            self.image=fire_anim[self.size][self.frame]
            self.rect= self.image.get_rect()
            self.rect.center= center
#classe das paredes
class wall(pygame.sprite.Sprite):
     
    def __init__(self, x,y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        wall_img = pygame.image.load(path.join(img_dir, "wall.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(wall_img, (50,50))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento. 
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        #self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.x = x
        # Sorteia um lugar inicial em y
        self.rect.y = y
#classe das bombas       
class Bomb1(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        bomb_img = pygame.image.load(path.join(img_dir, "bomb.png")).convert_alpha()#colocar a imagem da bomba
        self.image=bomb_img
        self.image=pygame.transform.scale(bomb_img,(35,35))        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        self.radius = int(self.rect.width * .55 / 2)

        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.x = x+10
        self.rect.y = y
        self.speedy = 0
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy 
        
# Inicialização do Pygame.

    

# Nome do jogo
pygame.display.set_caption("InsperBomb")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()


# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'hellfundo.png')).convert()#colocar o mapa do jogo
background=pygame.transform.scale(background, (480,600))#transforma a escala do png
background_rect = background.get_rect()

#Música
pygame.mixer.music.load(path.join(snd_dir, 'theme.mp3'))
pygame.mixer.music.set_volume(0.8)
boom_sound = pygame.mixer.Sound(path.join(snd_dir,'explio.wav'))
death_sound = pygame.mixer.Sound(path.join(snd_dir,'death.wav'))
#animação do jogador1
player1_anim={}
player1_anim['front']=[]
for a in np.arange(1,3,1):
    filename='pl1_front{0}.png'.format(a)
    img=pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img, (40,40))
    player1_anim['front'].append(img_lg)
  
#carrega animação jogador 2
player2_anim={}
player2_anim['front2']=[]
for a in np.arange(1,3,1):
    filename='pl2_front{0}.png'.format(a)
    img=pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img, (40,40))
    player2_anim['front2'].append(img_lg)

#animacão do fogo
fire_anim={}
fire_anim['fire']=[]
for a in np.arange(1,3,1):
    filename='fire_anim{0}.png'.format(a)
    img=pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img, (50,50))
    fire_anim['fire'].append(img_lg)

#carrega a imagem das explosões
explosion_anim={}
explosion_anim['lg']=[]
explosion_anim['sm']=[]
for i in np.arange(1,14,1):
    filename='Explosion-{0}.png.png'.format(i)
    img=pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img, (120,120))
    explosion_anim['lg'].append(img_lg)
    

# Carrega os sons do jogo
'''pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))#colocar os sons
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))#arrumar som
destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))#arrumar som
pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))#arrumar som'''

# Cria um jogador. O construtor será chamado automaticamente
player1 =Player1('front')
player2=Player2('front2')

# Cria um grupo de todos os sprites e adiciona ao player.
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

#cria um grupo para as explosões
exp=pygame.sprite.Group()
#Cria um grupo só dos meteoros
mobs = pygame.sprite.Group()

# Posição das paredes no mapa
bombs = pygame.sprite.Group()
walls = pygame.sprite.Group() 
x=53.3333
y=53.33333

for d in range(16):
    m=wall(x,y)
    all_sprites.add(m)
    walls.add(m)
    x+=106.33333333333333
    if x>=450:
        x=53.333333
        y+=160
        
# Cria 8 meteoros e adiciona no grupo meteoros
for i in range(1):
    m = Mob('fire')
    all_sprites.add(m)
    mobs.add(m)


    
    
        
        
# Comando para evitar travamentos.
try:
    
    # Loop principal.
    
    pygame.mixer.music.play(loops=-1)
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
                    player1.speedx = -5
                if event.key == pygame.K_RIGHT:
                    player1.speedx = 5
                if event.key==pygame.K_UP:
                    player1.speedy=- 5
                if event.key==pygame.K_DOWN:
                    player1.speedy=5
                if event.key==pygame.K_w:
                    player2.speedy=-5
                if event.key==pygame.K_s:
                    player2.speedy=5
                if event.key==pygame.K_a:
                    player2.speedx=-5
                if event.key==pygame.K_d:
                    player2.speedx=5
                 # Se for um espaço atira!
                if event.key == pygame.K_SPACE:
                    if player1.speedx>0:
                        bomb = Bomb1(player1.rect.left, player1.rect.bottom)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
                    elif player1.speedx<0:
                        bomb = Bomb1(player1.rect.right, player1.rect.top)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
                    elif player1.speedy>0:
                        bomb = Bomb1(player1.rect.centerx, player1.rect.top)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
                    else:
                        bomb = Bomb1(player1.rect.centerx, player1.rect.bottom)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
                    
                    
                    '''
                    pew_sound.play()'''
                if event.key == pygame.K_e :
                  
                    if player2.speedx>0:
                        bomb = Bomb1(player2.rect.left, player2.rect.bottom)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
                    elif player2.speedx<0:
                        bomb = Bomb1(player2.rect.right, player2.rect.top)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
                    elif player2.speedy>0:
                        bomb = Bomb1(player2.rect.centerx, player2.rect.top)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
                    elif player2.speedy<0: 
                        bomb = Bomb1(player2.rect.centerx, player2.rect.bottom)
                        all_sprites.add(bomb)
                        bombs.add(bomb)
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
        #jogodores não conseguem passar pela parede
        parede2 = pygame.sprite.spritecollide(player2, walls, False)        
        parede = pygame.sprite.spritecollide(player1, walls, False)
        for s in parede:
            if player1.speedx >0:
                player1.rect.right = s.rect.left
                player1.speedx=0
            if player1.speedx<0:
                player1.rect.left = s.rect.right
                player1.speedx=0
            if player1.speedy>0:
                player1.rect.bottom=s.rect.top
                player1.speedy=0
            if player1.speedy<0:
                player1.rect.top=s.rect.bottom
                player1.speedy=0
       
        for s in parede2:
            if player2.speedx >0:
                player2.rect.right = s.rect.left
                player2.speedx=0
            if player2.speedx<0:
                player2.rect.left = s.rect.right
                player2.speedx=0
            if player2.speedy>0:
                player2.rect.bottom=s.rect.top
                player2.speedy=0
            if player2.speedy<0:
                player2.rect.top=s.rect.bottom
                player2.speedy=0
        bomba=pygame.sprite.spritecollide(player1,bombs,False)
        bomba2=pygame.sprite.spritecollide(player2,bombs,False)
        
        for s in bomba:
            if player1.speedx >0:
                player1.rect.right = s.rect.left
                player1.speedx=0
            if player1.speedx<0:
                player1.rect.left = s.rect.right
                player1.speedx=0
            if player1.speedy>0:
                player1.rect.bottom=s.rect.top
                player1.speedy=0
            if player1.speedy<0:
                player1.rect.top=s.rect.bottom
                player1.speedy=0
       
        for s in bomba2:
            if player2.speedx >0:
                player2.rect.right = s.rect.left
                player2.speedx=0
            if player2.speedx<0:
                player2.rect.left = s.rect.right
                player2.speedx=0
            if player2.speedy>0:
                player2.rect.bottom=s.rect.top
                player2.speedy=0
            if player2.speedy<0:
                player2.rect.top=s.rect.bottom
                player2.speedy=0
          
    
                    
        # Depois de processar os eventos.
        # Atualiza a ação de cada sprite.
        all_sprites.update()
        
        # Verifica se houve colisão entre tiro e meteoro
        hits = pygame.sprite.groupcollide(mobs, bombs, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            
            boom_sound.play()
            expl=Explosion(hit.rect.center, 'lg')
            exp.add(expl)
            all_sprites.add(expl)
            m = Mob('fire') 
            all_sprites.add(m)
            mobs.add(m)
        
        hits1 = pygame.sprite.spritecollide(player1, exp, False, pygame.sprite.collide_circle)
        hits2 = pygame.sprite.spritecollide(player2, exp, False, pygame.sprite.collide_circle)
        if hits1 or hits2:
            # Toca o som da colisão
            death_sound.play()
            time.sleep(1)
            '''
            boom_sound.play()'''
            running=False
            # Precisa esperar se não fecha
        
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

           