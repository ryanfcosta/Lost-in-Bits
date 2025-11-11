from PPlay import sprite
from constants import UP, LEFT, RIGHT, DOWN

class Entity:    
    def __init__(self, window, level):
        self.window = window
        self.level = level
        self.velocity_x = None
        self.velocity_y = None
        self.direction_x = None
        self.direction_y = None
        self.x_left_limit = 0
        self.x_right_limit = self.window.width
    
    def setup_sprite(self, assets_path, sprite_image):
        self.sprite = sprite.Sprite(f"assets/{assets_path}{sprite_image}.png")
    
    def move(self, delta_time):
        pass
    
    def is_on_horizontal_limit(self, direction):
        if direction == LEFT:
            return self.sprite.x <= self.x_left_limit
        elif direction == RIGHT:
            return (self.sprite.x + self.sprite.width) >= self.x_right_limit
        return None
    
    def is_on_vertical_limit(self, direction):
        if direction == UP:
            return self.sprite.y <= 0
        elif direction == DOWN:
            return (self.sprite.y + self.sprite.height) >= self.level.floor_y
        return None
    
    def set_direction_x(self, direction_x):
        if direction_x is not None:
            self.direction_x = direction_x
