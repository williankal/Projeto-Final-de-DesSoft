import pygame
from config import *
from Bomb import Bomb

class Player(pygame.sprite.Sprite):
    def __init__(self, size, player_anim, spawn):
        pygame.sprite.Sprite.__init__(self)
        self.player_anim = player_anim
        self.size=size
        self.image=self.player_anim[self.size][1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = spawn[0]
        self.rect.top = spawn[1]
        self.speed = 5
        self.speedx = 0
        self.speedy = 0
        self.radius=10
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
        self.collision_tolerance = 10
        
    def move(self, direction):
        """Moves the player towards a direction.

        Args:
            direction (str): The direction the player is about to move.
                The directions are: 'left', 'right', 'up', 'down'.
        """
        if direction == 'left':
            self.speedx = -self.speed
        if direction == 'right':
            self.speedx = self.speed
        if direction == 'up':
            self.speedy = -self.speed
        if direction == 'down':
            self.speedy = self.speed

    def stop(self, axis):
        """Stops the player movement.

        Args:
            axis (str): The axis that will have the movement stopped.
        """
        if axis == 'x':
            self.speedx = 0
        if axis == 'y':
            self.speedy = 0

    def avoid_collision(self, collider):
        """Avoids the collision between the player and a collider.

        Args:
            collider (object): The object the player is colliding with.
        """

        if abs(collider.rect.top - self.rect.bottom) < self.collision_tolerance and self.speedy > 0:
            self.rect.bottom = collider.rect.top-1
            self.speedy = 0
        if abs(collider.rect.bottom - self.rect.top) < self.collision_tolerance and self.speedy < 0:
            self.rect.top = collider.rect.bottom+1
            self.speedy = 0
        if abs(collider.rect.left - self.rect.right) < self.collision_tolerance and self.speedx > 0:
            self.rect.right = collider.rect.left-1
            self.speedx = 0
        if abs(collider.rect.right - self.rect.left) < self.collision_tolerance and self.speedx < 0:
            self.rect.left = collider.rect.right+1
            self.speedx = 0

    def plant_bomb(self, all_sprites, bombs):
        bomb = Bomb(self.rect.centerx, self.rect.centery)
        all_sprites.add(bomb)
        bombs.add(bomb)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
        if self.rect.top < 0:
            self.rect.top=0

        now = pygame.time.get_ticks()
        if now - self.last_update>self.frame_rate:
            self.last_update= now
            self.frame +=1
            if self.frame==len(self.player_anim[self.size]):
                self.frame=0

            center= self.rect.center
            self.image=self.player_anim[self.size][self.frame]
            self.rect= self.image.get_rect()
            self.rect.center= center