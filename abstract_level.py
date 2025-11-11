from PPlay import sprite

class AbstractLevel:
    def __init__(self, window, assets_path, background_image, floor_relative_height):
        self.window = window
        self.assets_path = assets_path
        self.background = sprite.Sprite(f"assets/{assets_path}/{background_image}.png")
        self.floor_y = window.height * floor_relative_height
    
    def load_level(self):
        self.npcs = []