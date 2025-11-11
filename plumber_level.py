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