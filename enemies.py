import pygame
import random
from settings import *
from entities import *
from items import *

class Reaper(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = 2
        self.vy = 0
        self.throwing = False
        self.blade_count = 700
        self.direction = 0
        self.distancex = 0
        self.distancey = 0
        self.hitting = False
        
    def show_blade(self):
        if self.throwing and self.blade_count > 0 and self.image_index >= len(self.images) and len(self.game.enemy_blades) == 0:
            selfrecleft = self.rect.left
            selfrectop = self.rect.top
            loc = [selfrecleft / 64, selfrectop / 64]
            b = Blade(self.game, blade_1_img, loc, self.direction)
            self.game.enemy_blades.add(b)
            self.game.all_sprites.add(b)
            self.throwing = False
            self.blade_count -=1
            
    def check_player(self):
        self.distancex = self.game.hero.rect.centerx - self.rect.centerx
        self.distancey = self.game.hero.rect.centery - self.rect.centery
        if -200 < self.distancex < 200:
            self.throwing = False
            if self.game.hero.hitting == True and self.game.hero.image_index >= len(self.game.hero.images) and -50 < self.distancey < 50:
                self.kill()
                self.game.hero.powerup += 1
        elif -400 < self.distancex < 400 and -100 < self.distancey < 100:
            if self.distancex > 0:
                self.direction = 1
            else:
                self.direction = -1
            self.throwing = True
            
    def check_blades(self):
        hits = pygame.sprite.spritecollide(self, self.game.player_blades, True)
        for blade in hits:
            self.game.hero.score += 75 * self.game.level
            self.game.hero.powerup += 0.5
            self.kill()
            
    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_platform_edges()
        self.check_world_edges()
        self.animate()
        self.check_player()
        self.show_blade()
        self.check_blades()

class SandNinja(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vy = 0
        self.vx = 0
        self.jump_power = 18
        self.distancex = 0
        self.distancey = 0
        self.health = random.randint(1, 3)

        self.facing_right = False
        self.hitting = False

    def move_left(self):
        self.facing_right = False
        self.vx = -2

    def move_right(self):
        self.facing_right = True
        self.vx = 2

    def jump(self):
        pass

    def block(self):
        pass

    def hit(self):
        self.vx = 0
        self.hitting = True
        
    def stop(self):
        self.vx = 0
        self.hitting = False
        
    def check_player(self):
        self.distancex = self.game.hero.rect.centerx - self.rect.centerx
        self.distancey = self.game.hero.rect.centery - self.rect.centery
        if -100 < self.distancex < 100 and -100 < self.distancey < 100 and self.game.hero.hitting and self.game.hero.punch_landed == False and self.game.hero.image_index >= len(self.game.hero.images):
            self.health -= 1 * self.game.hero.power
            self.game.hero.punch_landed = True
            self.game.hero.powerup += 1
        if -100 < self.distancex < 100 and -100 < self.distancey < 100:
            self.hit()
        elif -400 < self.distancex < 400 and -100 < self.distancey < 100:
            self.move()
        else:
            self.stop()

    def check_blades(self):
        hits = pygame.sprite.spritecollide(self, self.game.player_blades, False)
        for blade in hits:
            self.health -= 0.5 * self.game.hero.power
            self.game.hero.powerup += 0.5
            blade.kill()

    def move(self):
        if self.distancex < 0:
            self.hitting = False
            self.move_left()
        elif self.distancex > 0:
            self.hitting = False
            self.move_right()
            
    def set_image_list(self):
        if self.facing_right:
            if self.hitting:
                self.images = enemy_2_hitting_images_2
            elif self.vx > 0:
                self.images = enemy_2_walk_images_2
            else:
                self.images = enemy_2_stance_images_2
        elif not self.facing_right:
            if self.hitting:
                self.images = enemy_2_hitting_images
            elif self.vx < 0:
                self.images = enemy_2_walk_images
            else:
                self.images = enemy_2_stance_images
                
    def live(self):
        if self.health <= 0:
            self.game.hero.score += 125 * self.game.level
            self.kill()

    def is_alive(self):
        return(self.health > 0)
    
    def update(self):
        if self.is_alive():
            self.apply_gravity()
            self.move_and_check_platforms()
            self.check_world_edges()
            self.check_player()
            self.animate()
            self.check_blades()
            self.live()
        else:
            pass

class SandNinja2(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = 0
        self.vy = 0
        self.throwing = False
        self.blade_count = 700
        self.direction = 0
        self.health = random.randint(1, 3)

        self.facing_right = False
        self.hitting = False
            
    def move_left(self):
        self.facing_right = False
        self.vx = -2

    def move_right(self):
        self.facing_right = True
        self.vx = 2

    def jump(self):
        pass

    def block(self):
        pass

    def hit(self):
        self.vx = 0
        self.hitting = True

    def throw(self):
        self.throwing = True
        
    def stop(self):
        self.vx = 0
        self.hitting = False

    def check_blades(self):
        hits = pygame.sprite.spritecollide(self, self.game.player_blades, True)
        for blade in hits:
            self.game.hero.score += 75 * self.game.level
            self.kill()
        
    def check_player(self):
        self.distancex = self.game.hero.rect.centerx - self.rect.centerx
        self.distancey = self.game.hero.rect.centery - self.rect.centery
        if -100 < self.distancex < 100 and -100 < self.distancey < 100 and self.game.hero.hitting and self.game.hero.punch_landed == False and self.game.hero.image_index >= len(self.game.hero.images):
            self.health -= 1 * self.game.hero.power
            self.game.hero.punch_landed = True
            self.game.hero.powerup += 1
        if -100 < self.distancex < 100 and -100 < self.distancey < 100:
            self.hit()
        elif -400 < self.distancex < 400 and -100 < self.distancey < 100:
            self.throw()
            if self.distancex > 0:
                self.direction = 1
            else:
                self.direction = -1
        else:
            self.stop()

    def show_blade(self):
        if self.throwing and self.blade_count > 0 and self.image_index >= len(self.images) and len(self.game.enemy_blades) == 0:
            selfrecleft = self.rect.left
            selfrectop = self.rect.top
            loc = [selfrecleft / 64, selfrectop / 64]
            b = Blade(self.game, blade_1_img, loc, self.direction)
            self.game.enemy_blades.add(b)
            self.game.all_sprites.add(b)
            self.throwing = False
            self.blade_count -=1
            
    def set_image_list(self):
        if self.facing_right:
            if self.hitting:
                self.images = enemy_2_hitting_images_2
            elif self.vx > 0:
                self.images = enemy_2_walk_images_2
            elif self.throwing:
                self.images = enemy_2_throw_images
            else:
                self.images = enemy_2_stance_images_2
        elif not self.facing_right:
            if self.hitting:
                self.images = enemy_2_hitting_images
            elif self.vx < 0:
                self.images = enemy_2_walk_images
            elif self.throwing:
                self.images = enemy_2_throw_images
            else:
                self.images = enemy_2_stance_images

    def live(self):
        if self.health == 0:
            self.game.hero.score += 125 * self.game.level
            self.kill()

    def is_alive(self):
        return(self.health > 0)
                
    def update(self):
        if self.is_alive():
            self.apply_gravity()
            self.move_and_check_platforms()
            self.check_world_edges()
            self.check_player()
            self.animate()
            self.show_blade()
            self.check_blades()
            self.live()
        else:
            pass


        
