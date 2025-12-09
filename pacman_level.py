from abstract_level import AbstractLevel
import game_platform
import pygame
from PPlay.sprite import Sprite
from ghost import Ghost 
from collections import deque 
from constants import STATES_PER_SECOND, REWIND_DURATION_SECS 

class BlackBackground:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
    
    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen.get_width(), screen.get_height()))

class PacmanLevel(AbstractLevel):
    floor_relative_height = 0.95
    level_name = "Don't Feed The Yellow"
    level_path = "level_2/"
    sprite_name = "floor_brick"
    
    def __init__(self, game, assets_path, background_image):
        self.game = game
        self.window = game.window
        self.assets_path = assets_path
        self.floor_relative_height = PacmanLevel.floor_relative_height
        self.floor_y = game.window.height * self.floor_relative_height
        self.background = BlackBackground(self.window.width, self.window.height)

        total_states = STATES_PER_SECOND * REWIND_DURATION_SECS
        self.states = deque(maxlen=total_states)

    def load_level(self):
        self.npcs = []
        self.platforms = []
        
        w = self.window.width
        h = self.window.height
        blk = 60 
        center_x = w / 2
        
        # chao
        p_floor = game_platform.Platform(self.window, self)
        p_floor.set_platform(0, h - blk, 32, self.level_path, self.sprite_name)
        self.platforms.append(p_floor)

        # laterais
        for i in range(1, 17): 
            y_pos = i * blk
            p_wall_l = game_platform.Platform(self.window, self)
            p_wall_l.set_platform(0, y_pos, 1, self.level_path, self.sprite_name)
            self.platforms.append(p_wall_l)
            p_wall_r = game_platform.Platform(self.window, self)
            p_wall_r.set_platform(w - blk, y_pos, 1, self.level_path, self.sprite_name)
            self.platforms.append(p_wall_r)

        

        # laterais de cima
        top_y = 200
        p_top_l = game_platform.Platform(self.window, self)
        p_top_l.set_platform(center_x - (6*blk), top_y, 3, self.level_path, self.sprite_name)
        self.platforms.append(p_top_l)
        p_top_r = game_platform.Platform(self.window, self)
        p_top_r.set_platform(center_x + (2*blk), top_y, 3, self.level_path, self.sprite_name)
        self.platforms.append(p_top_r)


        # BOWL
        bowl_y_base = 500 
        p_bowl_base = game_platform.Platform(self.window, self)
        p_bowl_base.set_platform(center_x - (8*blk), bowl_y_base, 15, self.level_path, self.sprite_name)
        self.platforms.append(p_bowl_base)
        for i in range(1, 4): 
            p_u_l = game_platform.Platform(self.window, self)
            p_u_l.set_platform(center_x - (8*blk), bowl_y_base - (i*blk), 1, self.level_path, self.sprite_name)
            self.platforms.append(p_u_l)      
            p_u_r = game_platform.Platform(self.window, self)
            p_u_r.set_platform(center_x + (6*blk), bowl_y_base - (i*blk), 1, self.level_path, self.sprite_name)
            self.platforms.append(p_u_r)

        # plat monstro
        side_y = 750
        p_float_l = game_platform.Platform(self.window, self)
        p_float_l.set_platform(blk * 5, side_y, 3, self.level_path, self.sprite_name)
        self.platforms.append(p_float_l)
        p_float_r = game_platform.Platform(self.window, self)
        p_float_r.set_platform(w - (blk * 8), side_y, 3, self.level_path, self.sprite_name)
        self.platforms.append(p_float_r)


        # plat pra pular pra plat mais alta
        p_lat_3l = game_platform.Platform(self.window, self)
        p_lat_3l.set_platform(center_x - (11 * blk), 440, 2, self.level_path, self.sprite_name)
        p_lat_3r = game_platform.Platform(self.window, self)
        p_lat_3r.set_platform(center_x + (9 * blk), 440, 2, self.level_path, self.sprite_name)
        self.platforms.append(p_lat_3r)
        self.platforms.append(p_lat_3l)

        p_lat_2l = game_platform.Platform(self.window, self)
        p_lat_2l.set_platform(center_x - (14 * blk), 550, 2, self.level_path, self.sprite_name)
        self.platforms.append(p_lat_2l)
        p_lat_2r = game_platform.Platform(self.window, self)
        p_lat_2r.set_platform(center_x + (12 * blk), 550, 2, self.level_path, self.sprite_name)
        self.platforms.append(p_lat_2r)

        #gaps
        gap_y = 770
        p_gap_l = game_platform.Platform(self.window, self)
        p_gap_l.set_platform(center_x - (7 * blk), gap_y, 2, self.level_path, self.sprite_name)
        self.platforms.append(p_gap_l)
        p_gap_r = game_platform.Platform(self.window, self)
        p_gap_r.set_platform(center_x + (5 * blk), gap_y, 2, self.level_path, self.sprite_name)
        self.platforms.append(p_gap_r)
        
        # associado ao do monstro
        p_xtra_l = game_platform.Platform(self.window, self)
        p_xtra_l.set_platform(blk * 5, side_y - 80, 2, self.level_path, self.sprite_name)
        self.platforms.append(p_xtra_l)
        p_xtra_r = game_platform.Platform(self.window, self)
        p_xtra_r.set_platform(w - (blk * 7), side_y - 80, 2, self.level_path, self.sprite_name)
        self.platforms.append(p_xtra_r)


        # feito mais embaixo
        bot_y = 893
        p_bot_long = game_platform.Platform(self.window, self)
        p_bot_long.set_platform(center_x - (12*blk), bot_y, 24, self.level_path, self.sprite_name)
        self.platforms.append(p_bot_long)

        # ghost bowl
        ghost1 = Ghost(self.game, center_x, 462, "assets/level_2/ghost.png")
        ghost1.speed = 0
        self.npcs.append(ghost1)
        
        ghost1_left = Ghost(self.game, center_x - (2*blk), 462, "assets/level_2/ghost.png")
        ghost1_left.speed = 0
        self.npcs.append(ghost1_left)
        
        ghost1_right = Ghost(self.game, center_x + (2*blk), 462, "assets/level_2/ghost.png")
        ghost1_right.speed = 0
        self.npcs.append(ghost1_right)

        # ghost plat direita
        ghost2 = Ghost(self.game, w - (blk * 8), 712, "assets/level_2/ghost.png")
        ghost2.speed = 0
        self.npcs.append(ghost2)

        # ghost plat esquerda
        ghost3 = Ghost(self.game, blk *  7, 712, "assets/level_2/ghost.png")
        ghost3.speed = 0 
        self.npcs.append(ghost3)

        # ghost chaser 
        ghost_chaser = Ghost(self.game, center_x, 893, "assets/level_2/ghost.png")
        self.npcs.append(ghost_chaser)


        self.door = Sprite("assets/level_2/door.png") 
        self.door.x = (w / 2) - (self.door.width / 2)
        self.door.y = 60 

    def set_player_start_position(self):
        self.game.level.player.sprite.x = self.window.width - 200
        self.game.level.player.sprite.y = self.window.height - 150

    def handle_player_collisions(self):
        if self.game.level.player.sprite.collided(self.door):
            print("Venceu a fase Pacman!")
            #level_3

        for npc in self.npcs:
            if self.game.level.player.sprite.collided(npc.sprite):
                self.load_level() 
                self.set_player_start_position()
                break