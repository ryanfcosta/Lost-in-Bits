from abstract_level import AbstractLevel
from goomba import Goomba

class PlumberLevel(AbstractLevel):
    floor_relative_height = 0.8
    level_name = "Plumber Level"
    
    def __init__(self, window, assets_path, background_image):
        super().__init__(window, assets_path, background_image, PlumberLevel.floor_relative_height)
    
    def load_level(self):
        super().load_level()
        goomba_1 = Goomba(self.window, self, self.assets_path, "goomba", left_limit=0.6, right_limit=0.8, pos_x=0.7)

        print(goomba_1.sprite.x, goomba_1.sprite.y)
        self.npcs.append(goomba_1)
    
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
                        print("player morre")