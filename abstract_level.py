from PPlay import sprite

class AbstractLevel:
    def __init__(self, game, assets_path, background_image, floor_relative_height):
        self.game = game
        self.window = game.window
        self.assets_path = assets_path
        self.background_image = background_image
        self.background = sprite.Sprite(f"assets/{assets_path}/{background_image}.png")
        self.floor_y = game.window.height * floor_relative_height
    
    def load_level(self):
        self.npcs = []