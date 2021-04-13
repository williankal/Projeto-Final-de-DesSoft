import pygame
from config import *

class Bomb(pygame.sprite.Sprite):
    
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
        self.rect.x = x
        self.rect.y = y
        self.speedy = 0

        self.bombExplosionTime = 5000 # milisegundos
        self.bombSpawnTime = pygame.time.get_ticks()
        self.bombTimer = self.bombSpawnTime + self.bombExplosionTime
    
    def explode(self):
        pass

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.bombSpawnTime = pygame.time.get_ticks()
        if self.bombSpawnTime >= self.bombTimer:
            self.explode()
