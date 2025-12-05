from abstract_level import AbstractLevel
from goomba import Goomba
from bullet import Bullet
from constants import UP, LEFT, RIGHT, DOWN


class PlumberLevel(AbstractLevel):
    floor_relative_height = 0.8
    level_name = "Plumber Level"
    
    def __init__(self, game, assets_path, background_image):
        super().__init__(game, assets_path, background_image, PlumberLevel.floor_relative_height)
    
    def load_level(self):
        super().load_level()
        goomba_1 = Goomba(self.window, self, self.assets_path, "goomba", left_limit=0.6, right_limit=0.8, pos_x=0.7)
        #bullet test
        bullet_1 = Bullet(self.window, self, self.assets_path, "bullet", 0.01, RIGHT) #sprite ainda ta mt pequeno

        print(bullet_1.sprite.x, bullet_1.sprite.y)
        self.npcs.append(goomba_1)
        self.npcs.append(bullet_1)
    
    def handle_player_collisions(self):
        player_min_x = self.player.sprite.x - self.background.x
        player_max_x = self.player.sprite.x + self.player.sprite.width - self.background.x
        player_top_y = self.player.sprite.y
        player_bottom_y = self.player.sprite.y + self.player.sprite.height

        for npc in self.npcs:
            npc_min_x = npc.sprite.x
            npc_max_x = npc.sprite.x + npc.sprite.width
            npc_top_y = npc.sprite.y
            npc_bottom_y = npc.sprite.y + npc.sprite.height

            if isinstance(npc, Goomba):
                if player_max_x > npc_min_x and player_min_x < npc_max_x:
                    y_tolerance = 0.005 * self.window.height
                    player_is_stomping_goomba = (player_bottom_y > npc_top_y) and (player_bottom_y <= (npc_top_y + y_tolerance))
                    if player_is_stomping_goomba:
                        npc.alive = False
                    elif (player_bottom_y > npc_top_y) and (player_top_y < npc_bottom_y) and npc.alive:
                        self.game.level = PlumberLevel.create_level_instance(self.game, self.assets_path, self.background_image)
                        self.game.setup_level()
            elif isinstance(npc, Bullet):
                is_touching_x_left = player_max_x == npc_max_x or player_max_x == npc_min_x
                is_touching_x_right = player_min_x == npc_max_x or player_min_x == npc_min_x
                is_touching_y_top = player_top_y == npc_top_y or player_top_y == npc_bottom_y
                is_touching_y_bottom = player_bottom_y == npc_top_y or player_bottom_y == npc_bottom_y

                if ((is_touching_x_left or is_touching_x_right) and (is_touching_y_top or is_touching_y_bottom)):
                    npc.alive = False #nao ta funcionando ainda rs

                
    def create_level_instance(game, assets_path, background_image):
        return PlumberLevel(game, assets_path, background_image)