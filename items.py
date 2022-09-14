import pygame
import random
from settings import *
from entities import *


class Coin(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.value = 100 * self.game.level
        
    def apply(self, character):
        character.score += self.value
        print(character.score)
        self.game.hero.powerup += 0.5

class Health(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.value = 50  * self.game.level
        
    def apply(self, character):
        health_lost = 10 - character.health
        amount = random.randint(0, health_lost)
        character.health += amount
        character.score += self.value
        self.game.hero.powerup += 0.5
        print(character.health)

class Tool_Refill(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.value = 50 * self.game.level

    def apply(self, character):
        character.blade_count = 5
        character.score += self.value
        self.game.hero.powerup += 0.5
        
class Key_1(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.value = 20  * self.game.level
        
    def apply(self, character):
        character.score +=  self.value
        print(character.score)
        character.has_key_1 = True

class Box_1(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.score = 200 * self.game.level
        self.used = False
        
    def apply(self, character):
        if character.has_key_1:
            self.image = box_open_img
            character.score += self.score
            character.has_key_1 = False
            self.used = True
            self.game.hero.powerup += 2
        elif self.used:
            self.image = box_open_img
        else:
            self.image = box_closed_img
        print(character.score)

class Respawn(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.orig_loc_x = 3
        self.orig_loc_y = 3
        
    def apply(self, character):
        character.rect.centerx = self.orig_loc_x * GRID_SIZE
        character.rect.centery = self.orig_loc_y * GRID_SIZE

class Blade(AnimatedEntity):
    def __init__(self, game, image, loc, direction):
        super().__init__(game, image, loc)
        self.timer = 25
        self.speed = 10 * direction

    def apply(self, character):
        character.health -= 1
        self.kill()
        
    def update(self):
        self.rect.centerx += self.speed
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.timer -= 1
        
        if self.timer == 0 or len(hits) > 0:
            self.kill()

        self.animate()
