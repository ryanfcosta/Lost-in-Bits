from abstract_level import AbstractLevel
import game_platform
import pygame
from PPlay.sprite import Sprite
from collections import deque
from constants import STATES_PER_SECOND, REWIND_DURATION_SECS
from entity import Entity
from barrel import Barrel 

class BlackBackground:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
    
    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen.get_width(), screen.get_height()))

# --- SPAWNER ---
class BarrelSpawner(Entity):
    def __init__(self, window, level, x, y, interval):
        super().__init__(window, level)
        self.x = x
        self.y = y
        self.timer = 0
        self.interval = interval
        self.sprite = Sprite("assets/level_4/barrel.png") 
        self.sprite.x = -1000

    def move(self, delta_time):
        self.timer += delta_time
        if self.timer >= self.interval:
            self.timer = 0
            self.spawn()
    
    def spawn(self):
        barrel = Barrel(self.window, self.level, self.x, self.y)
        self.level.npcs.append(barrel)

    def draw(self):
        pass 

class KongLevel(AbstractLevel):
    level_name = "Kong's Tower"
    level_path = "level_2/" 
    sprite_name = "floor_brick"
    
    def __init__(self, game, assets_path, background_image):
        self.game = game
        self.window = game.window
        self.assets_path = assets_path
        self.floor_y = game.window.height - 60
        self.background = BlackBackground(self.window.width, self.window.height)
        total_states = STATES_PER_SECOND * REWIND_DURATION_SECS
        self.states = deque(maxlen=total_states)

    def load_level(self):
        self.npcs = []
        self.platforms = []
        self.background.x = 0
        
        w = self.window.width
        h = self.window.height
        blk = 60 
        
        step_normal = 22
        step_steep = 40  
        
        p_floor = game_platform.Platform(self.window, self)
        p_floor.set_platform(0, h - blk, 32, self.level_path, self.sprite_name)
        self.platforms.append(p_floor)

        start_x_1 = w - (2 * blk)
        start_y_1 = h - (2 * blk) 
        
        steps_1 = 13 
        
        current_x = start_x_1
        current_y = start_y_1
        
        for i in range(steps_1):
            self.create_platform(current_x, current_y, 2)
            current_x -= (2 * blk)
            current_y -= step_normal

        end_x_1 = current_x
        end_y_1 = current_y + step_normal
        self.create_platform(end_x_1, end_y_1, 2)

        gap_size = 2.5 * blk 

        start_x_2 = end_x_1 + gap_size
        
        start_y_2 = end_y_1 - 20 
        
        steps_2 = 9 
        
        current_x_2 = start_x_2
        current_y_2 = start_y_2
        
        for i in range(steps_2):
            self.create_platform(current_x_2, current_y_2, 2)
            current_x_2 += (2 * blk)
            current_y_2 -= step_steep 

        top_y = current_y_2 + step_steep
        self.create_platform(w - (16 * blk), top_y, 16) 

        self.door = Sprite("assets/level_1/door.png")
        self.kong = Sprite("assets/level_4/kong.png")
        
        self.door.x = w - (8 * blk)
        self.door.y = top_y - self.door.height
        
        self.kong.x = self.door.x + self.door.width + 80
        self.kong.y = top_y - self.kong.height
        
        spawner1 = BarrelSpawner(self.window, self, self.kong.x, self.kong.y + 50, interval=2.0)
        self.npcs.append(spawner1)
        
        spawner2 = BarrelSpawner(self.window, self, w/2, 0, interval=3.0)
        self.npcs.append(spawner2)

    def create_platform(self, x, y, width_blocks):
        p = game_platform.Platform(self.window, self)
        p.set_platform(x, y, width_blocks, self.level_path, self.sprite_name)
        self.platforms.append(p)

    def draw(self, window):
        self.background.draw()
        for platform in self.platforms:
            platform.draw()
        self.door.draw()
        self.kong.draw()
        for npc in self.npcs:
            npc.draw()

    def set_player_start_position(self):
        self.game.level.player.sprite.x = self.window.width - 150
        self.game.level.player.sprite.y = self.window.height - 150

    def handle_player_collisions(self):
        player = self.game.level.player
        
        if player.sprite.collided(self.door):
            print("Venceu o Kong!")
            self.game.setup_level()

        player_rect = pygame.Rect(player.sprite.x, player.sprite.y, 
                                  player.sprite.width, player.sprite.height)
        hitbox = player_rect.inflate(-20, -20) 

        for npc in self.npcs:
            if isinstance(npc, BarrelSpawner) or not npc.alive: continue
            
            npc_rect = pygame.Rect(npc.sprite.x, npc.sprite.y, 
                                   npc.sprite.width, npc.sprite.height)
            
            if hitbox.colliderect(npc_rect):
                print("Esmagado por um barril!")
                self.game.setup_level()
                break