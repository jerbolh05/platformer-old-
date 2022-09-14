import pygame
import random
from settings import *


# Game objects
class Entity(pygame.sprite.Sprite):

    def __init__(self, game, image, loc=[0, 0]):
        super().__init__()
        self.image = image
        self.game = game
        self.rect = self.image.get_rect()
        self.move_to(loc)
        self.on_platform = False
        
    def move_to(self, loc):
        self.rect.centerx = loc[0] * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = loc[1] * GRID_SIZE + GRID_SIZE // 2
    def apply_gravity(self):
        self.vy += self.game.gravity
    def reverse(self):
        self.vx *= -1
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
    def move_and_check_platforms(self):
        self.rect.y += self.vy
##        if self.vy >= 0:
##            self.rect.y += 2
##        if self.vy > 0:
##            self.rect.y -= 2
        self.on_platform = False
        
        hits = pygame.sprite.spritecollide(self, self.game.boxes, False)
        for box in hits:
            box.apply(self)
            if self.vy < 0:
                self.rect.top = box.rect.bottom
            elif self.vy > 0:
                self.rect.bottom = box.rect.top
                self.on_platform = True
        if len(hits) > 0:
            self.vy = 0

        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for platform in hits:
            if self.vy < 0:
                self.rect.top = platform.rect.bottom
            elif self.vy > 0:
                self.rect.bottom = platform.rect.top
                self.on_platform = True
        if len(hits) > 0:
            self.vy = 0
        self.rect.x += self.vx
        
        hits = pygame.sprite.spritecollide(self, self.game.boxes, False)
        for box in hits:
            box.apply(self)
            if self.vx < 0:
                self.rect.left = box.rect.right
            elif self.vx > 0:
                self.rect.right = box.rect.left
        if len(hits) > 0:
            self.reverse()
                
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for platform in hits:
            if self.vx < 0:
                self.rect.left = platform.rect.right
            elif self.vx > 0:
                self.rect.right = platform.rect.left
        if len(hits) > 0:
            self.reverse()
    def check_platform_edges(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        at_edge = True
        for platform in hits:
            if self.vx < 0:
                if self.rect.left >= platform.rect.left:
                    at_edge = False
            elif self.vx > 0:
                if self.rect.right <= platform.rect.right:
                    at_edge = False
        if at_edge:
            self.reverse()
    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.reverse()
        elif self.rect.right > self.game.world_width:
            self.rect.right = self.game.world_width
            self.reverse()
        if self.rect.top > self.game.world_height:
            self.health = 0
            if hasattr(self, 'blade_count'):
                mad_snd.play()

class AnimatedEntity(Entity):
    def __init__(self, game, images, loc=[0, 0]):
        super().__init__(game, images[0], loc)
        self.images = images
        self.image_index = 0
        self.ticks = 0
        self.animation_speed = 7
        
    def set_image_list(self):
        self.images = self.images
        
    def animate(self):
        self.set_image_list()
        self.ticks += 1
        if self.ticks % self.animation_speed == 0:
            if self.image_index >= len(self.images):
                self.image_index = 0
                if hasattr(self, 'throwing'):
                    self.throwing = False
                    self.image_index = 0
            self.image = self.images[self.image_index]
            self.image_index += 1
