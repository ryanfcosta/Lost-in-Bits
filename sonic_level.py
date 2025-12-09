from abstract_level import AbstractLevel
import game_platform
import pygame
from PPlay.sprite import Sprite
from collections import deque
from constants import STATES_PER_SECOND, REWIND_DURATION_SECS
from goomba import Goomba 

class CyanBackground:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
    
    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 100, 100), (0, 0, screen.get_width(), screen.get_height()))

class SonicLevel(AbstractLevel):
    level_name = "Green Hills"
    level_path = "level_3/" 
    sprite_name = "floor_brick"
    
    def __init__(self, game, assets_path, background_image):
        self.game = game
        self.window = game.window
        self.assets_path = assets_path
        
        self.blk = 60
        self.map_blocks_width = 213 
        
        self.floor_y = game.window.height - self.blk 
        
        total_width = self.map_blocks_width * self.blk
        self.background = CyanBackground(total_width, self.window.height)

        total_states = STATES_PER_SECOND * REWIND_DURATION_SECS
        self.states = deque(maxlen=total_states)

        self.base_speed = None
        self.max_sonic_speed = 0.85 
        self.acceleration = 0.0005 

        self.title_color = (0, 0, 0)

    def load_level(self):
        self.npcs = []
        self.platforms = []
        self.background.x = 0 
        
        h = self.window.height
        blk = self.blk
        
        # chao
        p_floor = game_platform.Platform(self.window, self)
        p_floor.set_platform(0, h - blk, self.map_blocks_width, self.level_path, self.sprite_name)
        self.platforms.append(p_floor)

        # plat
        self.create_stairs(15, 3, direction=1) 
        self.create_platform(18 * 60, h - (4 * blk), 10) 

        self.create_wall(40, 1) 
        self.create_wall(50, 1)

        start_loop_blk = 75
        self.create_platform((start_loop_blk) * 60, h - (2 * blk), 2)
        self.create_platform((start_loop_blk + 3) * 60, h - (3 * blk), 2)
        self.create_platform((start_loop_blk + 6) * 60, h - (4 * blk), 2) 
        self.create_platform((start_loop_blk + 9) * 60, h - (3 * blk), 2)
        self.create_platform((start_loop_blk + 12) * 60, h - (2 * blk), 2)

        for i in range(0, 8):
            base_x = (110 + (i * 6)) * 60
            self.create_platform(base_x, h - (2.5 * blk), 3)

        self.create_platform(180 * 60, h - (4 * blk), 20) 
        self.create_stairs(175, 3, direction=1)

        #mtbug
        self.create_motobug(start_blk=25, end_blk=35)
        
        moto_plat = self.create_motobug(start_blk=18, end_blk=28)
        moto_plat.sprite.y = h - (4 * blk) - moto_plat.sprite.height

        self.create_motobug(start_blk=42, end_blk=48)

        moto_loop = self.create_motobug(start_blk=start_loop_blk+6, end_blk=start_loop_blk+8)
        moto_loop.sprite.y = h - (4 * blk) - moto_loop.sprite.height

        self.create_motobug(start_blk=92, end_blk=100) 
        self.create_motobug(start_blk=102, end_blk=110)
        self.create_motobug(start_blk=115, end_blk=125)
        self.create_motobug(start_blk=130, end_blk=140)
        
        moto_pad_1 = self.create_motobug(start_blk=122, end_blk=125) 
        moto_pad_1.sprite.y = h - (2.5 * blk) - moto_pad_1.sprite.height
        
        moto_pad_2 = self.create_motobug(start_blk=140, end_blk=143) 
        moto_pad_2.sprite.y = h - (2.5 * blk) - moto_pad_2.sprite.height

        moto_end = self.create_motobug(start_blk=180, end_blk=200)
        moto_end.sprite.y = h - (4 * blk) - moto_end.sprite.height

        # --- 4. PORTA FINAL ---
        self.door = Sprite("assets/level_1/door.png") 
        self.door.x = (self.map_blocks_width - 5) * blk 
        self.door.y = h - blk - self.door.height

    def draw(self, window):
        self.background.draw()
        for platform in self.platforms:
            platform.draw()
        for npc in self.npcs:
            npc.sprite.draw()
        self.door.draw()

    def create_platform(self, x, y, width_blocks):
        p = game_platform.Platform(self.window, self)
        p.set_platform(x, y, width_blocks, self.level_path, self.sprite_name)
        self.platforms.append(p)

    def create_wall(self, x_block, height_blocks):
        for i in range(1, height_blocks + 1):
             p = game_platform.Platform(self.window, self)
             p.set_platform(x_block * 60, self.window.height - (i * 60) - 60, 1, self.level_path, self.sprite_name)
             self.platforms.append(p)

    def create_stairs(self, start_block_x, height_steps, direction=1):
        h = self.window.height
        blk = self.blk
        for i in range(1, height_steps + 1):
            x = (start_block_x + (i * direction)) * blk
            y = h - ((i + 1) * blk) 
            self.create_platform(x, y, 1)

    def create_motobug(self, start_blk, end_blk):
        screen_w = self.window.width
        pos_start_norm = (start_blk * 60) / screen_w
        pos_end_norm = (end_blk * 60) / screen_w
        spawn_pos_norm = pos_start_norm 

        bug = Goomba(self.window, self, "level_3/", "motobug", 
                     left_limit=pos_start_norm, 
                     right_limit=pos_end_norm, 
                     pos_x=spawn_pos_norm)
        self.npcs.append(bug)
        return bug

    def set_player_start_position(self):
        self.game.level.player.sprite.x = 100
        self.game.level.player.sprite.y = self.window.height - 200

    def handle_player_collisions(self):
        player = self.game.level.player
        
        # Momentum
        if self.base_speed is None:
            self.base_speed = player.walking_vel_x
        if abs(player.velocity_x) > 0:
            if player.walking_vel_x < self.max_sonic_speed:
                player.walking_vel_x += self.acceleration
        else:
            if player.walking_vel_x != self.base_speed:
                player.walking_vel_x = self.base_speed

        if player.sprite.collided(self.door):
            print("Venceu a Green Hills!")
            player.walking_vel_x = self.base_speed

        for npc in self.npcs:
            npc.sprite.x += self.background.x

            if player.sprite.collided(npc.sprite):
                print("Foi pego pelo Motobug!")
                player.walking_vel_x = self.base_speed 
                self.game.setup_level() 
                break
            
            npc.sprite.x -= self.background.x