import pygame
from config import *

class Wall(pygame.sprite.Sprite):
     
    def __init__(self, x,y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        wall_img = pygame.image.load(path.join(img_dir, "wall.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(wall_img, (WALL_WIDTH, WALL_HEIGHT))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento. 
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        #self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.x = x
        # Sorteia um lugar inicial em y
        self.rect.y = y
            