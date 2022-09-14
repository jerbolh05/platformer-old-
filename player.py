import pygame
import random
from settings import *
from entities import *
from items import *

class Player(AnimatedEntity):
    def __init__(self, game, images):
        super().__init__(game, images)
        self.vx = 0
        self.vy = 0
        self.speed = 4
        self.power = 1
        self.jump_power = 18
        self.score = 0

        self.health = 10
        self.blade_count = 5
        self.escape_time = 30
        self.has_key_1 = False
        
        self.can_powerup = False
        self.has_powered_up = False
        self.powerup_counter = 500
        self.powerup = 0
        
        self.on_platform = False
        self.blocking = False
        self.throwing = False
        self.facing_right = True
        self.dashing = False
        self.dashing_left = False
        self.dashing_right = False
        self.jumping = False
        self.hitting = False
        self.punch_landed = False
        self.using_special_attack_1 = False
        self.charging = False
        
    def move_left(self):
        self.vx = -self.speed
        self.facing_right = False
        self.dashing_left = False
        self.dashing_right = False
        self.dashing = False
        
    def move_right(self):
        self.vx = self.speed
        self.facing_right = True
        self.dashing_right = False
        self.dashing_left = False
        self.dashing = False
        
    def block(self):
        self.blocking = True
        
    def throw(self):
        self.throwing = True
        self.image_index = 0

    def dash(self):
        if self.facing_right == False:
            self.dashing = True
            self.vx += -self.speed * 3
            self.dashing_left = True
            self.dashing_right = False
        elif self.facing_right == True:
            self.dashing = True
            self.vx += self.speed * 3
            self.dashing_left = False
            self.dashing_right = True
        self.image_index = 0

    def hit(self):
        self.punch_landed = False
        self.hitting = True
        self.image_index = 0

    def jump(self):
        self.jumping = True
        if self.on_platform:
            self.vy -= 1 * self.jump_power

    def charge(self):
        self.charging = True
        if self.ticks % self.animation_speed == 0:
            self.powerup += 0.1

    def power_up(self):
        self.has_powered_up = True
        self.speed = 10
        self.power = 5
        self.jump_power = 25
        self.health += 5
        self.powerup -= 5

    def use_special_attack_1(self):
        self.using_special_attack_1 = True
        self.image_index = 0
        
    def stop(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if self.dashing and self.image_index >= len(self.images) or self.using_special_attack_1 and self.image_index >= len(self.images):
            self.vx = 0
        elif not self.dashing and not self.using_special_attack_1:
            self.vx = 0
        elif self.using_special_attack_1 and len(hits) > 0:
            for enemy in hits:
                enemy.kill()
        self.jumping = False
        self.blocking = False
        self.charging = False
        if self.hitting == True and self.image_index >= len(self.images):
            self.hitting = False
        elif self.using_special_attack_1 and self.image_index >= len(self.images):
            self.using_special_attack_1 = False
        elif self.dashing_right == True and self.image_index >= len(self.images):
            self.dashing_left = False
            self.dashing_right = False
        elif self.dashing_left == True and self.image_index >= len(self.images):
            self.dashing_left = False
            self.dashing_right = False
            
    def check_items(self):
        hits = pygame.sprite.spritecollide(self, self.game.collectibles, True)
        for collectible in hits:
            collectible.apply(self)
            special_snd.play()
        hits = pygame.sprite.spritecollide(self, self.game.boxes, False)
        for box in hits:
            box.apply(self)
            treasure_snd.play()
        hits = pygame.sprite.spritecollide(self, self.game.respawns, False)
        for respawns in hits:
            respawns.apply(self)
        hits = pygame.sprite.spritecollide(self, self.game.ladders, False)
        for ladders in hits:
            ladders.apply(self)

    def check_signs(self):
        hits1 = pygame.sprite.spritecollide(self, self.game.message_1, False)
        hits2 = pygame.sprite.spritecollide(self, self.game.message_2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.message_3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.message_4, False)
        if len(hits1) > 0:
            self.game.on_message_1 = True
        elif len(hits2) > 0:
            self.game.on_message_2 = True
        elif len(hits3) > 0:
            self.game.on_message_3 = True
        elif len(hits4) > 0:
            self.game.on_message_4 = True
        else:
            self.game.on_message_1 = False
            self.game.on_message_2 = False
            self.game.on_message_3 = False
            self.game.on_message_4 = False
        
    def reached_goal(self):
        hits = pygame.sprite.spritecollide(self, self.game.goals, False)
        return len(hits) > 0
    
    def check_enemies(self):
        if self.escape_time == 0 and self.blocking == False:
            hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
            for enemy in hits:
                self.health -= 1
                hurt_snd.play()
                self.escape_time = 30
                if self.rect.centerx < enemy.rect.centerx:
                    self.vx -= 30
                    self.blocking = True
                elif self.rect.centerx > enemy.rect.centerx:
                    self.vx = 30
                    self.blocking = True
        for enemy in self.game.enemies:
            if enemy.hitting and self.escape_time == 0 and self.blocking == False:
                self.health -= 1
                hurt_snd.play()
                self.escape_time = 30
        if self.escape_time > 0:
            self.escape_time -= 1

    def check_blades(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemy_blades, False)
        for blade in hits:
            if self.blocking == False:
                self.health -= 1
                blade.kill()

    def is_alive(self):
        return self.health > 0
    
    def set_image_list(self):
        if self.facing_right and not self.has_powered_up:
            if not self.on_platform:
                self.images = player_jump_1_images
            elif self.dashing_right:
                self.images = player_dash_right_images
            elif self.using_special_attack_1:
                self.images = player_special_attack_1_right_images
            elif self.vx > 0:
                self.images = player_walk_right_images
            elif self.throwing:
                self.images = player_throw_images
            elif self.blocking:
                self.images = player_block_img
            elif self.hitting:
                self.images = player_hit_images
            elif self.charging:
                self.images = player_charge_image_1
            else:
                self.images = player_stance_right_images
        elif not self.facing_right and not self.has_powered_up:
            if not self.on_platform:
                self.images = player_jump_2_images
            elif self.dashing_left:
                self.images = player_dash_left_images
            elif self.using_special_attack_1:
                self.images = player_special_attack_1_left_images
            elif self.vx < 0:
                self.images = player_walk_left_images
            elif self.throwing:
                self.images = player_throw_2_images
            elif self.blocking:
                self.images = player_block_2_img
            elif self.hitting:
                self.images = player_hit_2_images
            elif self.charging:
                self.images = player_charge_image_2
            else:
                self.images = player_stance_left_images
        elif self.facing_right and self.has_powered_up:
            if not self.on_platform:
                self.images = player_jump_1_images
            elif self.vx > 0:
                self.images = player_powerup_walk_right_images
            elif self.throwing:
                self.images = player_throw_images
            elif self.blocking:
                self.images = player_block_img
            elif self.hitting:
                self.images = player_powerup_punch_images
            else:
                self.images = player_powerup_stance_images
        elif not self.facing_right and self.has_powered_up:
            if not self.on_platform:
                self.images = player_jump_2_images
            elif self.vx < 0:
                self.images = player_powerup_walk_left_images
            elif self.throwing:
                self.images = player_throw_2_images
            elif self.blocking:
                self.images = player_block_2_img
            elif self.hitting:
                self.images = player_powerup_punch_2_images
            else:
                self.images = player_powerup_stance_2_images
        
    def release_blade(self):
        if self.throwing and self.blade_count > 0 and self.image_index >= len(self.images) and self.jumping == False:
            
            if self.facing_right:
                direction = 1
                x = self.rect.right
                y = self.rect.top + 10
            else:
                x = self.rect.left
                y = self.rect.top + 10
                direction = -1

            loc = [x / 64, y / 64]
            b = Blade(self.game, blade_1_img, loc, direction)
            self.game.player_blades.add(b)
            self.game.all_sprites.add(b)
            throw_snd.play()
            self.throwing = False
            self.blade_count -=1

    def on_ladder(self):
        hits = pygame.sprite.spritecollide(self, self.game.ladders, False)
        return len(hits) > 0        

    def powerup_check(self):
        if self.has_powered_up:
            self.powerup_counter -= 1
            if self.powerup_counter == 0:
                self.has_powered_up = False
                self.powerup_counter = 500
                self.speed = 4
                self.power = 1
                self.jump_power = 18
                self.can_powerup = False
        if self.powerup >= 5:
            self.can_powerup = True

    def apply_special_attacks(self):
        if not self.has_powered_up:
            if self.facing_right and self.image_index >= 9 and self.using_special_attack_1:
                self.vx = 8
            elif not self.facing_right and self.image_index >= 9 and self.using_special_attack_1:
                self.vx = -8

    def not_moving(self):
        if self.vx == 0:
            return True

    def reverse(self):
        pass
        
    def update(self):
        if not self.on_ladder():
            self.apply_gravity()
        self.check_enemies()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.animate()
        self.release_blade()
        self.check_items()
        self.check_blades()
        self.check_signs()
        self.powerup_check()
        self.apply_special_attacks()
