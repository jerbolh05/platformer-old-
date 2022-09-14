# Imports
import pygame
from utilities import *


# Window settings
GRID_SIZE = 64
WIDTH = 20 * GRID_SIZE # 1280
HEIGHT = 10 * GRID_SIZE # 640
TITLE = "platformer-type-game"
FPS = 60


# Make the game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Define colors
SKY_BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
dark_gray = (26, 26, 26)

    
# Fonts
FONT_Comfortaa_Title = pygame.font.Font('assets/fonts/Comfortaa.ttf', 96)
FONT_Spacegrotesk_Title = pygame.font.Font('assets/fonts/SpaceGrotesk.ttf', 60)
FONT_Spacegrotesk_menu_screens = pygame.font.Font('assets/fonts/SpaceGrotesk.ttf', 26)
FONT_Spacegrotesk_menu_screen = pygame.font.Font('assets/fonts/PressStart2P.ttf', 26)
FONT_Spacegrotesk = pygame.font.Font('assets/fonts/SpaceGrotesk.ttf', 35)
FONT_LG = pygame.font.Font(None, 64)
FONT_MD = pygame.font.Font(None, 32)
FONT_SM = pygame.font.Font(None, 24)


# Load images

# ----- TILE IMAGES ----- #

background_img = load_image('assets/images/backgrounds/background.jpg')
block_img = load_image('assets/images/tiles/block.png')
block_left_img = load_image('assets/images/tiles/block_left.png')
block_middle_img = load_image('assets/images/tiles/block_middle.png')
block_right_img = load_image('assets/images/tiles/block_right.png')
grass_top_img = load_image('assets/images/tiles/grass_top.png')
grass_top_left_corner_img = load_image('assets/images/tiles/grass_top_left_corner.png')
grass_top_right_corner_img = load_image('assets/images/tiles/grass_top_right_corner.png')
grass_brown_top_img = load_image('assets/images/tiles/grass_brown_top.png')
grass_brown_top_left_img = load_image('assets/images/tiles/grass_brown_top_left.png')
grass_brown_top_right_img = load_image('assets/images/tiles/grass_brown_top_right.png')
dirt_img = load_image('assets/images/tiles/dirt.png')
dirt_bottom_img = load_image('assets/images/tiles/dirt_bottom.png')
dirt_bottom_right_img = load_image('assets/images/tiles/dirt_bottom_right.png')
dirt_bottom_left_img = load_image('assets/images/tiles/dirt_bottom_left.png')
dirt_right_img = load_image('assets/images/tiles/dirt_right.png')
dirt_left_img = load_image('assets/images/tiles/dirt_left.png')
dirt_top_right_img = load_image('assets/images/tiles/dirt_top_right.png')
dirt_top_left_img = load_image('assets/images/tiles/dirt_top_left.png')
dirt_bottom_right_1_img = load_image('assets/images/tiles/dirt_bottom_right_1.png')
dirt_top_right_1_img = load_image('assets/images/tiles/dirt_top_right_1.png')
block_img = load_image('assets/images/tiles/block.png')
arrow_right_img = load_image('assets/images/tiles/arrow_1.png')
arrow_left_img = load_image('assets/images/tiles/arrow_3.png')
arrow_down_img = load_image('assets/images/tiles/arrow_2.png')
tree_1_bottom_img = load_image('assets/images/tiles/tree_1_bottom.png')
tree_1_middle_1_img = load_image('assets/images/tiles/tree_1_middle_1.png')
tree_1_middle_2_img = load_image('assets/images/tiles/tree_1_middle_2.png')
tree_1_middle_3_img = load_image('assets/images/tiles/tree_1_middle_3.png')
tree_1_middle_4_img = load_image('assets/images/tiles/tree_1_middle_4.png')
tree_1_middle_5_img = load_image('assets/images/tiles/tree_1_middle_5.png')
tree_1_top_1_img = load_image('assets/images/tiles/tree_1_top_1.png')
tree_1_top_2_img = load_image('assets/images/tiles/tree_1_top_2.png')
tree_1_top_3_img = load_image('assets/images/tiles/tree_1_top_3.png')
tree_1_top_4_img = load_image('assets/images/tiles/tree_1_top_4.png')
tree_1_top_5_img = load_image('assets/images/tiles/tree_1_top_5.png')
tree_1_top_6_img = load_image('assets/images/tiles/tree_1_top_6.png')
tree_1_top_7_img = load_image('assets/images/tiles/tree_1_top_7.png')
tree_1_top_8_img = load_image('assets/images/tiles/tree_1_top_8.png')
tree_1_top_9_img = load_image('assets/images/tiles/tree_1_top_9.png')
tree_1_top_10_img = load_image('assets/images/tiles/tree_1_top_10.png')
tree_1_branch_1_img = load_image('assets/images/tiles/tree_1_branch_1.png')
tree_1_branch_2_img = load_image('assets/images/tiles/tree_1_branch_2.png')

# ----- ITEM IMAGES ----- #

coin_img = load_image('assets/images/items/coin.png')
key_img = load_image('assets/images/items/key.png')
box_closed_img = load_image('assets/images/items/key_box_closed.png')
box_open_img = load_image('assets/images/items/key_box_open.png')
backpack_img = load_image('assets/images/tiles/backpack.png')
inventory_empty_img = load_image('assets/images/items/inventory/empty.png')
inventory_one_blade_img = load_image('assets/images/items/inventory/one_blade.png')
inventory_two_blades_img = load_image('assets/images/items/inventory/two_blades.png')
inventory_three_blades_img = load_image('assets/images/items/inventory/three_blades.png')
inventory_four_blades_img = load_image('assets/images/items/inventory/four_blades.png')
inventory_five_blades_img = load_image('assets/images/items/inventory/five_blades.png')
inventory_five_blades_key1_img = load_image('assets/images/items/inventory/five_blades_and_key1.png')
inventory_four_blades_key1_img = load_image('assets/images/items/inventory/four_blades_and_key1.png')
inventory_three_blades_key1_img = load_image('assets/images/items/inventory/three_blades_and_key1.png')
inventory_two_blades_key1_img = load_image('assets/images/items/inventory/two_blades_and_key1.png')
inventory_one_blade_key1_img = load_image('assets/images/items/inventory/one_blade_and_key1.png')
tool_refill_img = load_image('assets/images/items/tool_refill.png')
health_img = load_image('assets/images/items/health.png')
cloud_left_img = load_image('assets/images/tiles/cloud_left.png')
cloud_middle_img = load_image('assets/images/tiles/cloud_middle.png')
cloud_right_img = load_image('assets/images/tiles/cloud_right.png')
wire_top_img = load_image('assets/images/tiles/wire_top.png')
wire_bottom_img = load_image('assets/images/tiles/wire_bottom.png')
wire_img = load_image('assets/images/tiles/wire.png')
platform_img = load_image('assets/images/tiles/platform.png')
platform_left_img = load_image('assets/images/tiles/platform_left.png')
platform_middle_img = load_image('assets/images/tiles/platform_middle.png')
platform_right_img = load_image('assets/images/tiles/platform_right.png')
goal_images = [load_image('assets/images/tiles/flag_1.png'),
                        load_image('assets/images/tiles/flag_2.png')]
goalpole_img = [load_image('assets/images/tiles/flagpole.png')]
ladder_img = load_image('assets/images/tiles/ladder.png')
ladder_top_img = load_image('assets/images/tiles/ladder_top.png')
sign_img = load_image('assets/images/tiles/sign.png')
save_villagers_sign_img = load_image('assets/images/tiles/save_villagers_sign.png')
smart_enemy_sign_img = load_image('assets/images/tiles/smart_enemy_sign.png')
ninjas_below_sign_img = load_image('assets/images/tiles/ninjas_below_sign.png')
throwing_enemy_sign_img = load_image('assets/images/tiles/throwing_enemy_sign.png')
message_back = load_image('assets/images/tiles/message_background.png')
wood_background_img = load_image('assets/images/tiles/wood_background.png')
wood_background_1_img = load_image('assets/images/tiles/wood_background_1.png')
wood_background_2_img = load_image('assets/images/tiles/wood_background_2.png')
wood_background_3_img = load_image('assets/images/tiles/wood_background_3.png')
wood_background_4_img = load_image('assets/images/tiles/wood_background_4.png')
wood_background_5_img = load_image('assets/images/tiles/wood_background_5.png')

# ----- PLAYER IMAGES ----- #

player_img = [load_image('assets/images/characters/player/stance_1.png')]
player_stance_right_images = [load_image('assets/images/characters/player/naruto_stance_1.png'),
                              load_image('assets/images/characters/player/naruto_stance_2.png'),
                              load_image('assets/images/characters/player/naruto_stance_3.png'),
                              load_image('assets/images/characters/player/naruto_stance_4.png')]
"""load_image('assets/images/characters/player/stance_3.png'),
load_image('assets/images/characters/player/stance_2.png'),
load_image('assets/images/characters/player/stance_1.png')]"""
player_stance_left_images = [flip_image_x(img) for img in player_stance_right_images]
player_walk_right_images = [load_image('assets/images/characters/player/naruto_run_1.png'),
                           load_image('assets/images/characters/player/naruto_run_2.png'),
                           load_image('assets/images/characters/player/naruto_run_3.png'),
                           load_image('assets/images/characters/player/naruto_run_4.png'),
                           load_image('assets/images/characters/player/naruto_run_5.png'),
                           load_image('assets/images/characters/player/naruto_run_6.png'),
                           load_image('assets/images/characters/player/naruto_run_7.png'),
                           load_image('assets/images/characters/player/naruto_run_8.png')]
player_walk_left_images = [flip_image_x(img) for img in player_walk_right_images]
player_dash_right_images = [load_image('assets/images/characters/player/naruto_dash_1.png'),
                            load_image('assets/images/characters/player/naruto_dash_2.png'),
                            load_image('assets/images/characters/player/naruto_dash_3.png'),
                            load_image('assets/images/characters/player/naruto_dash_4.png')]
player_dash_left_images = [flip_image_x(img) for img in player_dash_right_images]
player_block_img = [load_image('assets/images/characters/player/block_1.png')]
player_block_2_img = [flip_image_x(img) for img in player_block_img]
player_throw_images = [load_image('assets/images/characters/player/naruto_throw_1.png'),
                       load_image('assets/images/characters/player/naruto_throw_1.png'),
                       load_image('assets/images/characters/player/naruto_throw_2.png'),
                       load_image('assets/images/characters/player/naruto_throw_3.png')]
player_throw_2_images = [flip_image_x(img) for img in player_throw_images]
player_jump_1_images = [load_image('assets/images/characters/player/naruto_jump_1.png')]
player_jump_2_images = [flip_image_x(img) for img in player_jump_1_images]
player_hit_images = [load_image('assets/images/characters/player/naruto_hit_1.png'),
                     load_image('assets/images/characters/player/naruto_hit_2.png'),
                     load_image('assets/images/characters/player/naruto_hit_3.png')]
player_hit_2_images = [flip_image_x(img) for img in player_hit_images]
player_special_attack_1_right_images = [load_image('assets/images/characters/player/naruto_rasengan_1.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_2.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_3.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_4.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_5.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_6.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_7.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_8.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_9.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_10.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_11.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_12.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_13.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_14.png'),
                                  load_image('assets/images/characters/player/naruto_rasengan_15.png')]
player_special_attack_1_left_images = [flip_image_x(img) for img in player_special_attack_1_right_images]
player_charge_image_1 = [load_image('assets/images/characters/player/naruto_charge_1.png')]
player_charge_image_2 = [flip_image_x(img) for img in player_charge_image_1]

player_powerup_stance_images = [load_image('assets/images/characters/player/SPM_stance_1.png'),
                                load_image('assets/images/characters/player/SPM_stance_2.png'),
                                load_image('assets/images/characters/player/SPM_stance_3.png')]
player_powerup_stance_2_images = [flip_image_x(img) for img in player_powerup_stance_images]
player_powerup_walk_right_images = [load_image('assets/images/characters/player/SPM_run_1.png'),
                                    load_image('assets/images/characters/player/SPM_run_2.png'),
                                    load_image('assets/images/characters/player/SPM_run_3.png'),
                                    load_image('assets/images/characters/player/SPM_run_4.png')]
player_powerup_walk_left_images = [flip_image_x(img) for img in player_powerup_walk_right_images]
player_powerup_punch_images = [load_image('assets/images/characters/player/SPM_punch_1.png'),
                               load_image('assets/images/characters/player/SPM_punch_2.png'),
                               load_image('assets/images/characters/player/SPM_punch_3.png'),
                               load_image('assets/images/characters/player/SPM_punch_4.png'),
                               load_image('assets/images/characters/player/SPM_punch_5.png'),
                               load_image('assets/images/characters/player/SPM_punch_6.png')]
player_powerup_punch_2_images = [flip_image_x(img) for img in player_powerup_punch_images]

# ----- ENEMY IMAGES ----- #

reaper_images = [load_image('assets/images/characters/enemy_1_1.png'),
                  load_image('assets/images/characters/enemy_1_2.png')]
enemy_2_stance_images = [load_image('assets/images/characters/enemy_2_stance_1.png'),
                         load_image('assets/images/characters/enemy_2_stance_2.png'),
                         load_image('assets/images/characters/enemy_2_stance_3.png')]
enemy_2_stance_images_2 = [flip_image_x(img) for img in enemy_2_stance_images]
enemy_2_walk_images = [load_image('assets/images/characters/enemy_2_walk_1.png'),
                       load_image('assets/images/characters/enemy_2_walk_2.png'),
                       load_image('assets/images/characters/enemy_2_walk_3.png'),
                       load_image('assets/images/characters/enemy_2_walk_4.png'),
                       load_image('assets/images/characters/enemy_2_walk_5.png'),
                       load_image('assets/images/characters/enemy_2_walk_6.png')]
enemy_2_walk_images_2 = [flip_image_x(img) for img in enemy_2_walk_images]
enemy_2_block_images = [load_image('assets/images/characters/enemy_2_block_1.png')]
enemy_2_block_images_2 = [flip_image_x(img) for img in enemy_2_block_images]
enemy_2_hitting_images = [load_image('assets/images/characters/enemy_2_hit_1.png'),
                          load_image('assets/images/characters/enemy_2_hit_2.png'),
                          load_image('assets/images/characters/enemy_2_hit_3.png')]
enemy_2_hitting_images_2 = [flip_image_x(img) for img in enemy_2_hitting_images]
enemy_2_throw_images = [load_image('assets/images/characters/enemy_2_throw_1.png'),
                        load_image('assets/images/characters/enemy_2_throw_2.png'),
                        load_image('assets/images/characters/enemy_2_throw_3.png'),
                        load_image('assets/images/characters/enemy_2_throw_4.png')]
enemy_2_throw_images_2 = [flip_image_x(img) for img in enemy_2_throw_images]

health_0_img = load_image('assets/images/characters/player/health_0.png')
health_1_img = load_image('assets/images/characters/player/health_1.png')
health_2_img = load_image('assets/images/characters/player/health_2.png')
health_3_img = load_image('assets/images/characters/player/health_3.png')
health_4_img = load_image('assets/images/characters/player/health_4.png')
health_5_img = load_image('assets/images/characters/player/health_5.png')
health_6_img = load_image('assets/images/characters/player/health_6.png')
health_7_img = load_image('assets/images/characters/player/health_7.png')
health_8_img = load_image('assets/images/characters/player/health_8.png')
health_9_img = load_image('assets/images/characters/player/health_9.png')
health_full_img = load_image('assets/images/characters/player/health_full.png')
powerup_0_img = load_image('assets/images/characters/player/powerup_0.png')
powerup_1_img = load_image('assets/images/characters/player/powerup_1.png')
powerup_2_img = load_image('assets/images/characters/player/powerup_2.png')
powerup_3_img = load_image('assets/images/characters/player/powerup_3.png')
powerup_4_img = load_image('assets/images/characters/player/powerup_4.png')
powerup_5_img = load_image('assets/images/characters/player/powerup_5.png')
powerup_6_img = load_image('assets/images/characters/player/powerup_6.png')
powerup_7_img = load_image('assets/images/characters/player/powerup_7.png')
powerup_8_img = load_image('assets/images/characters/player/powerup_8.png')
powerup_9_img = load_image('assets/images/characters/player/powerup_9.png')
powerup_10_img = load_image('assets/images/characters/player/powerup_10.png')
powerup_full_img = load_image('assets/images/characters/player/powerup_full.png')

blade_1_img = [load_image('assets/images/items/tools/blade_1.png')]
blade_images = [load_image('assets/images/items/tools/blade_1.png'),
                load_image('assets/images/items/tools/blade_2.png'),
                load_image('assets/images/items/tools/blade_3.png'),
                load_image('assets/images/items/tools/blade_4.png')]


# Load sounds
boo_snd = pygame.mixer.Sound('assets/sounds/boo.ogg')
mad_snd = pygame.mixer.Sound('assets/sounds/aw_shit.ogg')
throw_snd = pygame.mixer.Sound('assets/sounds/throw.ogg')
special_snd = pygame.mixer.Sound('assets/sounds/special.ogg')
treasure_snd = pygame.mixer.Sound('assets/sounds/box.ogg')
hurt_snd = pygame.mixer.Sound('assets/sounds/hurt.ogg')
rasengan_snd = pygame.mixer.Sound('assets/sounds/rasengan.ogg')

# Load music
theme_music = ('assets/music/background_music.ogg')

# Levels
levels = ['assets/levels/world-1.json',
          'assets/levels/world-2.json',
          'assets/levels/world-3.json',
          'assets/levels/world-4.json']

# Other constants and settings
START = 0
PLAYING = 1
PAUSED = 2
WIN = 3
LOSE = 4
PLAYING_TUTORIAL = 5
