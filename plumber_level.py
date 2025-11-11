from abstract_level import AbstractLevel
from goomba import Goomba
import game_platform
from PPlay import sprite
import pygame

class PlumberLevel(AbstractLevel):
    floor_relative_height = 0.8
    level_name = "Plumber Level"
    sprite_name = "floor_brick"
    level_path = "level_1/"
    #floor brick 60x60
        
    def __init__(self, game, assets_path, background_image):
        super().__init__(game, assets_path, background_image, PlumberLevel.floor_relative_height)
    
    def load_level(self):
        super().load_level()
        goomba_1 = Goomba(self.window, self, self.assets_path, "goomba", left_limit=0.6, right_limit=0.8, pos_x=0.7)
        goomba_2 = Goomba(self.window, self, self.assets_path, "goomba", left_limit=0.9, right_limit=1, pos_x=0.95)

        print(goomba_1.sprite.x, goomba_1.sprite.y)
        self.npcs.append(goomba_1)
        self.npcs.append(goomba_2)

        self.door = sprite.Sprite("assets/level_1/door.png")
        self.door.x = 5610
        self.door.y = self.floor_y - self.door.height

        self.platforms = []

        h_stair = 804 
        h_pipe = 744 
        h_high = 750

        plataforma_1 = game_platform.Platform(self.window, self)
        plataforma_1.set_platform(800, h_high, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_1)
        
        plataforma_2 = game_platform.Platform(self.window, self)
        plataforma_2.set_platform(920, h_high, 3, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_2)

        plataforma_3 = game_platform.Platform(self.window, self)
        plataforma_3.set_platform(1220, h_high, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_3)

        plataforma_4 = game_platform.Platform(self.window, self)
        plataforma_4.set_platform(1040, 650, 1, self.level_path, self.sprite_name) # Bloco 'escondido'
        self.platforms.append(plataforma_4)

        plataforma_5 = game_platform.Platform(self.window, self)
        plataforma_5.set_platform(1600, h_pipe, 2, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_5)

        plataforma_6 = game_platform.Platform(self.window, self)
        plataforma_6.set_platform(1840, h_pipe, 3, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_6)

        plataforma_7 = game_platform.Platform(self.window, self)
        plataforma_7.set_platform(2200, h_pipe, 2, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_7)

        plataforma_8 = game_platform.Platform(self.window, self)
        plataforma_8.set_platform(2600, h_stair, 4, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_8)

        plataforma_9 = game_platform.Platform(self.window, self)
        plataforma_9.set_platform(2660, 744, 3, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_9)

        plataforma_10 = game_platform.Platform(self.window, self)
        plataforma_10.set_platform(2720, 684, 2, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_10)

        plataforma_11 = game_platform.Platform(self.window, self)
        plataforma_11.set_platform(2780, 624, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_11)

        plataforma_12 = game_platform.Platform(self.window, self)
        plataforma_12.set_platform(3060, 624, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_12)

        plataforma_13 = game_platform.Platform(self.window, self)
        plataforma_13.set_platform(3120, 684, 2, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_13)
        
        plataforma_14 = game_platform.Platform(self.window, self)
        plataforma_14.set_platform(3180, 744, 3, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_14)

        plataforma_15 = game_platform.Platform(self.window, self)
        plataforma_15.set_platform(3600, h_pipe, 3, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_15)

        plataforma_16 = game_platform.Platform(self.window, self)
        plataforma_16.set_platform(3900, h_pipe, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_16)

        plataforma_17 = game_platform.Platform(self.window, self)
        plataforma_17.set_platform(4140, h_pipe, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_17)
        
        plataforma_18 = game_platform.Platform(self.window, self)
        plataforma_18.set_platform(4380, h_pipe, 2, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_18)

        plataforma_19 = game_platform.Platform(self.window, self)
        plataforma_19.set_platform(4700, h_pipe, 2, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_19)
        
        plataforma_20 = game_platform.Platform(self.window, self)
        plataforma_20.set_platform(4900, h_stair, 8, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_20)

        plataforma_21 = game_platform.Platform(self.window, self)
        plataforma_21.set_platform(4960, 744, 7, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_21)

        plataforma_22 = game_platform.Platform(self.window, self)
        plataforma_22.set_platform(5020, 684, 6, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_22)

        plataforma_23 = game_platform.Platform(self.window, self)
        plataforma_23.set_platform(5080, 624, 5, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_23)

        plataforma_24 = game_platform.Platform(self.window, self)
        plataforma_24.set_platform(5140, 564, 4, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_24)

        plataforma_25 = game_platform.Platform(self.window, self)
        plataforma_25.set_platform(5200, 504, 3, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_25)

        plataforma_26 = game_platform.Platform(self.window, self)
        plataforma_26.set_platform(5260, 444, 2, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_26)

        plataforma_27 = game_platform.Platform(self.window, self)
        plataforma_27.set_platform(5320, 384, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_27)
        
        plataforma_28 = game_platform.Platform(self.window, self)
        plataforma_28.set_platform(5440, h_stair, 1, self.level_path, self.sprite_name)
        self.platforms.append(plataforma_28)
    
    def handle_player_collisions(self):
        player_min_x = self.player.sprite.x - self.background.x
        player_max_x = self.player.sprite.x + self.player.sprite.width - self.background.x
        player_top_y = self.player.sprite.y
        player_bottom_y = self.player.sprite.y + self.player.sprite.height
        for npc in self.npcs:
            if isinstance(npc, Goomba):
                goomba_min_x = npc.sprite.x
                goomba_max_x = npc.sprite.x + npc.sprite.width
                goomba_top_y = npc.sprite.y
                goomba_bottom_y = npc.sprite.y + npc.sprite.height
                if player_max_x > goomba_min_x and player_min_x < goomba_max_x:
                    y_tolerance = 0.005 * self.window.height
                    player_is_stomping_goomba = (player_bottom_y > goomba_top_y) and (player_bottom_y <= (goomba_top_y + y_tolerance))
                    if player_is_stomping_goomba:
                        npc.alive = False
                    elif (player_bottom_y > goomba_top_y) and (player_top_y < goomba_bottom_y) and npc.alive:
                        self.game.level = PlumberLevel.create_level_instance(self.game, self.assets_path, self.background_image)
                        self.game.setup_level()
        
        if (self.player.sprite.x > self.door.x) and ((self.player.sprite.x + self.player.sprite.width) > (self.door.x + self.door.width)) and (self.player.sprite.y > self.door.y):
            pygame.quit()
            exit()
    
    def create_level_instance(game, assets_path, background_image):
        return PlumberLevel(game, assets_path, background_image)