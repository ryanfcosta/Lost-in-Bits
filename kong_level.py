from abstract_level import AbstractLevel
import game_platform
import pygame
from PPlay.sprite import Sprite
from collections import deque
from constants import STATES_PER_SECOND, REWIND_DURATION_SECS
from entity import Entity
from barrel import Barrel
import plumber_level

class BlackBackground:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
    
    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen.get_width(), screen.get_height()))

#spawner de barril
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
    level_name = "Monkey King"
    level_path = "level_4/" 
    sprite_name = "floor_brick"
    
    def __init__(self, game, assets_path, background_image):
        self.game = game
        self.window = game.window
        self.assets_path = assets_path
        
        self.floor_y = game.window.height - 60
        self.background = BlackBackground(self.window.width, self.window.height)
        
        total_states = STATES_PER_SECOND * REWIND_DURATION_SECS
        self.states = deque(maxlen=total_states)
        self.title_color = (255, 255, 255)

    def load_level(self):
        self.npcs = []
        self.platforms = []
        self.background.x = 0
        
        w = self.window.width
        h = self.window.height
        blk = 60 
        
        step_normal = 22 
        step_steep = 60
        
        # floor
        p_floor = game_platform.Platform(self.window, self)
        p_floor.set_platform(0, h - blk, 32, self.level_path, self.sprite_name)
        self.platforms.append(p_floor)

        # primeira escada
        start_x_1 = w - (2 * blk)
        start_y_1 = h - (2 * blk) 
        steps_1 = 13 
        current_x = start_x_1
        current_y = start_y_1
        
        for i in range(steps_1):
            self.create_platform(current_x, current_y, 2)
            current_x -= (2 * blk)
            current_y -= step_normal 

        # conexao
        end_x_1 = current_x
        end_y_1 = current_y + step_normal
        self.create_platform(end_x_1, end_y_1, 2)

        gap_size = 2.5 * blk 

        # segunda
        start_x_2 = end_x_1 + gap_size
        
        start_y_2 = end_y_1 - 120 
        
        steps_2 = 9 
        
        current_x_2 = start_x_2
        current_y_2 = start_y_2
        
        for i in range(steps_2):
            self.create_platform(current_x_2, current_y_2, 2)
            current_x_2 += (2 * blk) 
            current_y_2 -= step_steep 

        #final
        top_y = current_y_2 +  blk
        self.create_platform(w - (7.5 * blk), top_y, 10) 
        self.door = Sprite("assets/level_1/door.png")
        self.kong = Sprite("assets/level_4/kong.png")
        
        self.door.x = w - (2 * blk)
        self.door.y = top_y - self.door.height
        
        self.kong.x = self.door.x - self.door.width + 120
        self.kong.y = top_y - self.door.height +45
        
        spawner1 = BarrelSpawner(self.window, self, self.kong.x, 0, interval=1.0)
        self.npcs.append(spawner1)
        
        spawner2 = BarrelSpawner(self.window, self, w/2, 0, interval=2.0)
        self.npcs.append(spawner2)
    
        spawner3 = BarrelSpawner(self.window, self, self.kong.y, 0, interval=2.0)
        self.npcs.append(spawner3)

        cartridge_sprite = Sprite("assets/cartridge.png")
        cartridge_h = cartridge_sprite.height
        cart_1_x = blk * 2
        cart_1_y = h - blk - cartridge_h
        cart_2_i = 3
        cart_2_x = start_x_1 - (cart_2_i * 2 * blk) + blk 
        cart_2_y = start_y_1 - (cart_2_i * step_normal) - cartridge_h
        cart_3_x = end_x_1 + blk
        cart_3_y = end_y_1 + step_normal - cartridge_h - 20
        cart_5_x = w - (7 * blk) 
        cart_5_y = top_y - cartridge_h
        cartridge_positions = [
            (cart_1_x, cart_1_y), (cart_2_x, cart_2_y), (cart_3_x, cart_3_y), 
            (cart_5_x, cart_5_y)
        ]
        self.cartridges = []
        for x, y in cartridge_positions:
            cartridge = Sprite("assets/cartridge.png")
            cartridge.x = x
            cartridge.y = y
            self.cartridges.append(cartridge)

        cooler_sprite = Sprite("assets/frozen.png")
        cooler_h = cooler_sprite.height
        cool_1_i = 1 
        cool_1_x = start_x_1 - (cool_1_i * 2 * blk) + blk 
        cool_1_y = start_y_1 - (cool_1_i * step_normal) - cooler_h
        cool_3_x = end_x_1 + gap_size + blk
        cool_3_y = start_y_2 - cooler_h
        cool_4_i = 3
        cool_4_x = start_x_2 + (cool_4_i * 2 * blk) + blk
        cool_4_y = start_y_2 - (cool_4_i * step_steep) - cooler_h
        cool_5_x = self.door.x - blk
        cool_5_y = top_y - cooler_h
        cooler_positions = [
            (cool_1_x, cool_1_y), (cool_3_x, cool_3_y), 
            (cool_4_x, cool_4_y), (cool_5_x, cool_5_y)
        ]
        self.coolers = []
        for x, y in cooler_positions:
            cooler = Sprite("assets/frozen.png")
            cooler.x = x
            cooler.y = y
            self.coolers.append(cooler)

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
            self.game.menu = "main_menu"
            self.game.level = plumber_level.PlumberLevel(self.game, "level_1/", "background")
            self.game.setup_level() 

        player_rect = pygame.Rect(player.sprite.x, player.sprite.y, 
                                  player.sprite.width, player.sprite.height)
        
        hitbox = player_rect.inflate(-20, -20) 

        for npc in self.npcs:
            if isinstance(npc, BarrelSpawner) or not npc.alive: continue
            
            npc_rect = pygame.Rect(npc.sprite.x, npc.sprite.y, 
                                   npc.sprite.width, npc.sprite.height)
            
            if hitbox.colliderect(npc_rect):
                self.game.setup_level()
                break