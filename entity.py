from PPlay import sprite
from main import UP, LEFT, RIGHT, DOWN

class Entity:
    velocity_x = 0
    velocity_y = 0
    jump_force = 0
    direction_x = None
    direction_y = None
    
    def __init__(self, window, level, gravity):
        self.window = window
        self.level = level
        self.gravity = gravity
    
    def setup_sprite(self, assets_path, sprite_image):
        self.sprite = sprite.Sprite(f"assets/{assets_path}{sprite_image}.png")
    
    def move(self, delta_time):
        pass
    
    def is_on_horizontal_limit(self, direction):
        if direction == LEFT:
            return self.sprite.x <= 0
        elif direction == RIGHT:
            return (self.sprite.x + self.sprite.width) >= self.window.width
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
