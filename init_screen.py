import pygame
import random
from os import path

from config import img_dir, WHITE , FPS, GAME, QUIT


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

def final_screen(screen,hits1,hits2):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'p1_win.png')).convert()
    background=pygame.transform.scale(background,(480,600))
    background_rect = background.get_rect()

    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        if hits1:
            background = pygame.image.load(path.join(img_dir, 'p2_win.png')).convert()
            background=pygame.transform.scale(background,(480,600))
            state = QUIT
            running = False

        if hits2:
            background = pygame.image.load(path.join(img_dir, 'player1_win.png')).convert()
            background=pygame.transform.scale(background,(480,600))
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
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state