# Imports
import json
import pygame

from settings import *
from utilities import *
from entities import *
from items import *
from player import *
from enemies import *
from dummies import *

# Main game class 
class Game:

    def __init__(self):
        self.running = True
        self.grid_on = False
        self.new_game()
        self.inventory_shown = False
        self.random1 = 0
        self.on_message_1 = False
        self.on_message_2 = False
        self.on_message_3 = False
        self.on_message_4 = False
        self.on_message_5 = False
        self.music_count = 0
        self.music_num = 0

    def new_game(self):
        self.player = pygame.sprite.GroupSingle()
        self.hero = Player(self, player_img)
        self.player.add(self.hero)
        self.stage = START
        self.level = 1
        self.start_level()
        
    def start_level(self):
        
        self.platforms = pygame.sprite.Group()
        self.walk_thru = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()
        self.respawns = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.player_blades = pygame.sprite.Group()
        self.enemy_blades = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.ladders = pygame.sprite.Group()
        self.message_1 = pygame.sprite.Group()
        self.message_2 = pygame.sprite.Group()
        self.message_3 = pygame.sprite.Group()
        self.message_4 = pygame.sprite.Group()
        self.message_5 = pygame.sprite.Group()
        
        with open(levels[self.level - 1]) as f:
            data = json.load(f)
        self.world_width = data['width'] * GRID_SIZE
        self.world_height = data['height'] * GRID_SIZE
        self.gravity = data['gravity']
        loc = data['start']
        self.hero.move_to(loc)
        
        for loc in data['grass_top_left_corner_locs']:
            self.platforms.add( Platform(self, grass_top_left_corner_img, loc) )
        for loc in data['grass_top_locs']:
            self.platforms.add( Platform(self, grass_top_img, loc) )
        for loc in data['grass_top_right_corner_locs']:
            self.platforms.add( Platform(self, grass_top_right_corner_img, loc) )
        for loc in data['block_locs']:
            self.platforms.add( Platform(self, block_img, loc) )
        for loc in data['dirt_locs']:
            self.platforms.add( Platform(self, dirt_img, loc) )
        for loc in data['dirt_bottom_locs']:
            self.platforms.add( Platform(self, dirt_bottom_img, loc) )
        for loc in data['dirt_right_locs']:
            self.platforms.add( Platform(self, dirt_right_img, loc) )
        for loc in data['dirt_left_locs']:
            self.platforms.add( Platform(self, dirt_left_img, loc) )
        for loc in data['dirt_top_right_locs']:
            self.platforms.add( Platform(self, dirt_top_right_img, loc) )
        for loc in data['dirt_top_left_locs']:
            self.platforms.add( Platform(self, dirt_top_left_img, loc) )
        for loc in data['dirt_bottom_right_locs']:
            self.platforms.add( Platform(self, dirt_bottom_right_img, loc) )
        for loc in data['dirt_bottom_left_locs']:
            self.platforms.add( Platform(self, dirt_bottom_left_img, loc) )
        for loc in data['grass_brown_top_locs']:
            self.platforms.add(Platform(self, grass_brown_top_img, loc) )
        for loc in data['grass_brown_top_left_locs']:
            self.platforms.add(Platform(self, grass_brown_top_left_img, loc) )
        for loc in data['grass_brown_top_right_locs']:
            self.platforms.add(Platform(self, grass_brown_top_right_img, loc) )
        for loc in data['dirt_bottom_right_1_locs']:
            self.platforms.add( Platform(self, dirt_bottom_right_1_img, loc) )
        for loc in data['dirt_top_right_1_locs']:
            self.platforms.add( Platform(self, dirt_top_right_1_img, loc) )
        for loc in data['respwan_block_locs']:
            self.respawns.add( Respawn(self, block_img, loc) )
        for loc in data['block_left_locs']:
            self.platforms.add( Platform(self, block_left_img, loc) )
        for loc in data['block_middle_locs']:
            self.platforms.add( Platform(self, block_middle_img, loc) )
        for loc in data['block_right_locs']:
            self.platforms.add( Platform(self, block_right_img, loc) )
        for loc in data['block_locs']:
            self.platforms.add( Platform(self, block_img, loc) )
        for loc in data['platform_locs']:
            self.platforms.add( Platform(self, platform_img, loc) )
        for loc in data['platform_left_locs']:
            self.platforms.add( Platform(self, platform_left_img, loc) )
        for loc in data['platform_middle_locs']:
            self.platforms.add( Platform(self, platform_middle_img, loc) )
        for loc in data['platform_right_locs']:
            self.platforms.add( Platform(self, platform_right_img, loc) )
        for loc in data['box_1_locs']:
            self.boxes.add( Box_1(self, box_closed_img, loc) )
        for loc in data['cloud_left_locs']:
            self.walk_thru.add( WalkThru(self, cloud_left_img, loc) )
        for loc in data['cloud_middle_locs']:
            self.walk_thru.add( WalkThru(self, cloud_middle_img, loc) )
        for loc in data['cloud_right_locs']:
            self.walk_thru.add( WalkThru(self, cloud_right_img, loc) )
        for loc in data['arrow_down_locs']:
            self.walk_thru.add( WalkThru(self, arrow_down_img, loc) )
        for loc in data['wire_top_locs']:
            self.walk_thru.add( WalkThru(self, wire_top_img, loc) )
        for loc in data['wire_locs']:
            self.walk_thru.add( WalkThru(self, wire_img, loc) )
        for loc in data['wire_bottom_locs']:
            self.walk_thru.add( WalkThru(self, wire_bottom_img, loc) )
        for loc in data['arrow_right_locs']:
            self.walk_thru.add( WalkThru(self, arrow_right_img, loc) )
        for loc in data['arrow_left_locs']:
            self.walk_thru.add( WalkThru(self, arrow_left_img, loc) )
        for loc in data['tree_1_bottom']:
            self.walk_thru.add( WalkThru(self, tree_1_bottom_img, loc) )
        for loc in data['tree_1_middle_1']:
            self.walk_thru.add( WalkThru(self, tree_1_middle_1_img, loc) )
        for loc in data['tree_1_middle_2']:
            self.walk_thru.add( WalkThru(self, tree_1_middle_2_img, loc) )
        for loc in data['tree_1_middle_5']:
            self.walk_thru.add( WalkThru(self, tree_1_middle_5_img, loc) )
        for loc in data['tree_1_top_1']:
            self.walk_thru.add( WalkThru(self, tree_1_top_1_img, loc) )
        for loc in data['tree_1_top_2']:
            self.walk_thru.add( WalkThru(self, tree_1_top_2_img, loc) )
        for loc in data['tree_1_top_3']:
            self.walk_thru.add( WalkThru(self, tree_1_top_3_img, loc) )
        for loc in data['tree_1_top_4']:
            self.walk_thru.add( WalkThru(self, tree_1_top_4_img, loc) )
        for loc in data['tree_1_top_5']:
            self.walk_thru.add( WalkThru(self, tree_1_top_5_img, loc) )
        for loc in data['tree_1_top_6']:
            self.walk_thru.add( WalkThru(self, tree_1_top_6_img, loc) )
        for loc in data['tree_1_top_7']:
            self.walk_thru.add( WalkThru(self, tree_1_top_7_img, loc) )
        for loc in data['tree_1_top_8']:
            self.walk_thru.add( WalkThru(self, tree_1_top_8_img, loc) )
        for loc in data['tree_1_top_9']:
            self.walk_thru.add( WalkThru(self, tree_1_top_9_img, loc) )
        for loc in data['tree_1_top_10']:
            self.walk_thru.add( WalkThru(self, tree_1_top_10_img, loc) )
        for loc in data['tree_1_branch_2']:
            self.walk_thru.add( WalkThru(self, tree_1_branch_2_img, loc) )
        for loc in data['ladder_top_locs']:
            self.ladders.add( Ladder1(self, ladder_top_img, loc) )
        for loc in data['ladder_locs']:
            self.ladders.add( Ladder1(self, ladder_img, loc) )
        for loc in data['coin_locs']:
            self.collectibles.add( Coin(self, coin_img, loc) )
        for loc in data['key_1_locs']:
            self.collectibles.add( Key_1(self, key_img, loc) )
        for loc in data['tool_refill_locs']:
            self.collectibles.add( Tool_Refill(self, tool_refill_img, loc) )
        for loc in data['health_locs']:
            self.collectibles.add( Health(self, health_img, loc) )
        for n, loc in enumerate(data['goal_locs']):
            if n == 0:
                image = goal_images
            else:
                image = goalpole_img
            self.goals.add( Goal(self, image, loc) )
        for loc in data['reaper_locs']:
            self.enemies.add( Reaper(self, reaper_images, loc) )
        for loc in data['sand_ninja_locs']:
            self.enemies.add( SandNinja(self, enemy_2_stance_images, loc) )
        for loc in data['sand_ninja_2_locs']:
            self.enemies.add( SandNinja2(self, enemy_2_stance_images, loc) )
        for loc in data['message_1_locs']:
            self.message_1.add( Message(self, sign_img, loc) )
        for loc in data['message_2_locs']:
            self.message_2.add( Message(self, sign_img, loc) )
        for loc in data['message_3_locs']:
            self.message_3.add( Message(self, sign_img, loc) )
        for loc in data['message_4_locs']:
            self.message_4.add( Message(self, sign_img, loc) )
        for loc in data['message_5_locs']:
            self.message_5.add( Message(self, sign_img, loc) )
        for loc in data['wood_background_locs']:
            self.walk_thru.add( WalkThru(self, wood_background_img, loc) )
        for loc in data['wood_background_1_locs']:
            self.walk_thru.add( WalkThru(self, wood_background_1_img, loc) )
        for loc in data['wood_background_2_locs']:
            self.walk_thru.add( WalkThru(self, wood_background_2_img, loc) )
        for loc in data['wood_background_3_locs']:
            self.walk_thru.add( WalkThru(self, wood_background_3_img, loc) )
        for loc in data['wood_background_4_locs']:
            self.walk_thru.add( WalkThru(self, wood_background_4_img, loc) )
        for loc in data['wood_background_5_locs']:
            self.walk_thru.add( WalkThru(self, wood_background_5_img, loc) )
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.walk_thru, self.player, self.platforms, self.collectibles, self.boxes, self.respawns, self.goals, self.enemies, self.ladders, self.message_1, self.message_2, self.message_3)
        
    def show_title_screen(self):
        pygame.draw.rect(screen, dark_gray, [10, 160, 1260, 280])
        text = FONT_Spacegrotesk_Title.render("Press 'Enter' to start.", True, dark_gray)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 + 116
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screen.render("W, A, S, or arrow keys to move", True, WHITE)
        rect = text.get_rect()
        rect.left = 50
        rect.top = HEIGHT // 2 - 126
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screen.render("E - throw, Q - hit, C - charge", True, WHITE)
        rect = text.get_rect()
        rect.left = 50
        rect.top = HEIGHT // 2 - 86
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screen.render("1 and 2 for special attacks", True, WHITE)
        rect = text.get_rect()
        rect.left = 50
        rect.top = HEIGHT // 2 - 46
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screen.render("Try to get to the end", True, WHITE)
        rect = text.get_rect()
        rect.left = 50
        rect.top = HEIGHT // 2 - 6
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screen.render("Thank you for playing!", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 + 66
        screen.blit(text, rect)

    def show_win_screen(self):
        pygame.draw.rect(screen, dark_gray, [10, 180, 1260, 210])
        if self.random1 == 1:
            text = FONT_Spacegrotesk_menu_screens.render("Nice! But maybe next time hurry up, that was kind of boring...", True, WHITE)
        elif self.random1 == 2:
            text = FONT_Spacegrotesk_menu_screens.render("You won. . . Finally..", True, WHITE)
        elif self.random1 == 3:
            text = FONT_Spacegrotesk_menu_screens.render("My grandma coulda done better than that.... teh", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 116
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screens.render("Your score is: " + str(self.hero.score), True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 56
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screens.render("Press 'R' to start again.", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 26
        screen.blit(text, rect)
        
    def show_lose_screen(self):
        pygame.draw.rect(screen, dark_gray, [10, 180, 1260, 160])
        if self.random1 == 1:
            text = FONT_Spacegrotesk_menu_screens.render("Maybe, next time you can do better..?", True, WHITE)
        elif self.random1 == 2:
            text = FONT_Spacegrotesk_menu_screens.render("Is that really the best you got? ...", True, WHITE)
        elif self.random1 == 3:
            text = FONT_Spacegrotesk_menu_screens.render("My grandma coulda done better than that.... pfft", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 116
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screens.render("Your score is: " + str(self.hero.score), True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 56
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screens.render("Press 'R' to start again.", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 26
        screen.blit(text, rect)

    def show_pause_screen(self):
        pygame.draw.rect(screen, dark_gray, [10, 180, 1260, 160])
        if self.random1 == 1:
            text = FONT_Spacegrotesk_menu_screens.render("Come on, hurry up. Watching you play is like watching paint dry.", True, WHITE)
        elif self.random1 == 2:
            text = FONT_Spacegrotesk_menu_screens.render("Oh, hey there", True, WHITE)
        elif self.random1 == 3:
            text = FONT_Spacegrotesk_menu_screens.render("Oh! My grandma just finished for the third time while you JUST figured out how to pause..", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 116
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screens.render("Press 'p' key to continue", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 26
        screen.blit(text, rect)
    
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    self.grid_on = not self.grid_on
                if self.stage == START:
                    if event.key == pygame.K_RETURN:
                        self.stage = PLAYING
                        play_music(theme_music)
                elif self.stage == PLAYING:
                    if event.key == pygame.K_p:
                        self.stage = PAUSED
                        self.random1 = random.randint(1, 3)
                        pause_music()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w and not self.hero.has_powered_up:
                        self.hero.jump()
                    elif event.key == pygame.K_e and not self.hero.has_powered_up and self.hero.not_moving():
                        self.hero.throw()
                    elif event.key == pygame.K_q:
                        self.hero.hit()
                    elif event.key == pygame.K_x and not self.hero.has_powered_up:
                        self.hero.dash()
                    elif event.key == pygame.K_m and self.music_num == 0:
                        pause_music()
                        self.music_num += 1
                    elif event.key == pygame.K_m and self.music_num == 1:
                        unpause_music()
                        self.music_num -= 1
                    elif event.key == pygame.K_1 and self.hero.can_powerup and not self.hero.has_powered_up:
                        self.hero.power_up()
                    elif event.key == pygame.K_2 and self.hero.powerup >= 2.5 and not self.hero.has_powered_up:
                        self.hero.powerup -= 2.5
                        self.hero.use_special_attack_1()
                        rasengan_snd.play()
                    elif event.key == pygame.K_i and self.inventory_shown == False:
                        self.inventory_shown = True
                    elif event.key == pygame.K_i and self.inventory_shown:
                        self.inventory_shown = False
                    else:
                        self.hero.stop()
                elif self.stage == WIN or self.stage == LOSE:
                    if event.key == pygame.K_r:
                        self.new_game()
                elif self.stage == PAUSED:
                    if event.key == pygame.K_p:
                        self.stage = PLAYING
                        unpause_music()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_c]:
            self.hero.charge()
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self.hero.move_left()
        elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.hero.move_right()
        else:
            self.hero.stop()

    def update(self):
        if self.stage == PLAYING:
            self.all_sprites.update()
            if self.hero.reached_goal():
                if self.level < len(levels):
                    self.level += 1
                    self.start_level()
                    self.hero.has_key_1 = False
                else:
                    self.stage = WIN
                    self.random1 = random.randint(1, 3)
            elif not self.hero.is_alive():
                self.stage = LOSE
                self.random1 = random.randint(1, 3)
                pause_music()
            
    def get_offsets(self):
        
        if self.hero.rect.centerx < WIDTH // 2:
            offset_x = 0
        elif self.hero.rect.centerx > self.world_width - WIDTH // 2:
            offset_x = self.world_width - WIDTH
        else:
            offset_x = self.hero.rect.centerx - WIDTH // 2
            
        if self.hero.rect.centery - 250 < HEIGHT // 2:
            offset_y = 0
        elif self.hero.rect.centery > self.world_height - HEIGHT // 2:
            offset_y = self.world_height - HEIGHT
        else:
            offset_y = self.hero.rect.centery - HEIGHT // 2
            
        return offset_x, offset_y

    def render(self):
        offset_x, offset_y = self.get_offsets()
        screen.blit(background_img, (0, 0))
        if self.on_message_1:
            screen.blit(save_villagers_sign_img, (390, 25))
        elif self.on_message_2:
            screen.blit(smart_enemy_sign_img, (390, 25))
        elif self.on_message_3:
            screen.blit(ninjas_below_sign_img, (390, 25))
        elif self.on_message_4:
            screen.blit(throwing_enemy_sign_img, (390, 25))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])
        
        if self.stage == START:
            self.show_title_screen()
        elif self.stage == WIN:
            self.show_win_screen()
        elif self.stage == LOSE:
            mad_snd.play()
            self.show_lose_screen()
        elif self.stage == PAUSED:
            self.show_pause_screen()

        self.show_hud()
        if self.inventory_shown == True:
            if self.hero.blade_count == 5 and self.hero.has_key_1:
                screen.blit(inventory_five_blades_key1_img, (64, 320))
            elif self.hero.blade_count == 4 and self.hero.has_key_1:
                screen.blit(inventory_four_blades_key1_img, (64, 320))
            elif self.hero.blade_count == 3 and self.hero.has_key_1:
                screen.blit(inventory_three_blades_key1_img, (64, 320))
            elif self.hero.blade_count == 2 and self.hero.has_key_1:
                screen.blit(inventory_two_blades_key1_img, (64, 320))
            elif self.hero.blade_count == 1 and self.hero.has_key_1:
                screen.blit(inventory_one_blade_key1_img, (64, 320))
            elif self.hero.blade_count == 5:
                screen.blit(inventory_five_blades_img, (64, 320))
            elif self.hero.blade_count == 4:
                screen.blit(inventory_four_blades_img, (64, 320))
            elif self.hero.blade_count == 3:
                screen.blit(inventory_three_blades_img, (64, 320))
            elif self.hero.blade_count == 2:
                screen.blit(inventory_two_blades_img, (64, 320))
            elif self.hero.blade_count == 1:
                screen.blit(inventory_one_blade_img, (64, 320))
            else:
                screen.blit(inventory_empty_img, (64, 320))

        if self.grid_on:
            draw_grid(screen, WIDTH, HEIGHT, GRID_SIZE, offset_x, offset_y, color=RED)

    def show_hud(self):
        if self.hero.health > 10:
            health_img = health_full_img
        elif self.hero.health == 10:
            health_img = health_full_img
        elif self.hero.health == 9:
            health_img = health_9_img
        elif self.hero.health == 8:
            health_img = health_8_img
        elif self.hero.health == 7:
            health_img = health_7_img
        elif self.hero.health == 6:
            health_img = health_6_img
        elif self.hero.health == 5:
            health_img = health_5_img
        elif self.hero.health == 4:
            health_img = health_4_img
        elif self.hero.health == 3:
            health_img = health_3_img
        elif self.hero.health == 2:
            health_img = health_2_img
        elif self.hero.health == 1:
            health_img = health_1_img
        else:
            health_img = health_0_img
        if self.hero.powerup >= 5:
            powerup_img = powerup_full_img
        elif 4.5 <= self.hero.powerup <= 5:
            powerup_img = powerup_10_img
        elif 4 <= self.hero.powerup <= 4.5:
            powerup_img = powerup_9_img
        elif 3.5 <= self.hero.powerup <= 4:
            powerup_img = powerup_8_img
        elif 3 <= self.hero.powerup <= 3.5:
            powerup_img = powerup_7_img
        elif 2.5 <= self.hero.powerup <= 3:
            powerup_img = powerup_6_img
        elif 2 <= self.hero.powerup <= 2.5:
            powerup_img = powerup_5_img
        elif 1.5 <= self.hero.powerup <= 2:
            powerup_img = powerup_4_img
        elif 1 <= self.hero.powerup <= 1.5:
            powerup_img = powerup_3_img
        elif 0.5 <= self.hero.powerup <= 1:
            powerup_img = powerup_2_img
        elif 0 < self.hero.powerup <= 0.5:
            powerup_img = powerup_1_img
        elif self.hero.powerup <= 0:
            powerup_img = powerup_0_img
        if self.hero.powerup > 5:
            self.hero.powerup = 5
        elif self.hero.powerup < 0:
            self.hero.powerup = 0
        if self.hero.health > 10:
            self.hero.health = 10
        elif self.hero.health < 0:
            self.hero.health = 0
        screen.blit(health_img, (10, 0 ))
        screen.blit(powerup_img, (10, 0 ))
        
    def play(self):
        while self.running:
            self.process_input()     
            self.update()     
            self.render()            
            pygame.display.update()
            clock.tick(FPS)

# Let's do this!
if __name__ == "__main__":
   g = Game()
   g.play()
   pygame.quit()   
