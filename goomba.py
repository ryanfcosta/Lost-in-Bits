from entity import Entity
from constants import UP, LEFT, RIGHT, DOWN

class Goomba(Entity):
    walking_vel_x = 1

    def __init__(self, window, level, assets_path, sprite_image, left_limit, right_limit, pos_x):
        super().__init__(window, level)
        self.velocity_x = self.walking_vel_x
        self.direction_x = LEFT
        self.alive = True
        self.setup_sprite(assets_path, sprite_image)
        self.x_left_limit = left_limit
        self.x_right_limit = right_limit
        self.sprite.x = pos_x * window.width
        self.sprite.y = level.floor_y - self.sprite.height
    
    def move(self, delta_time):
        if self.is_on_horizontal_limit(LEFT) or self.is_on_horizontal_limit(RIGHT):
            self.direction_x *= -1
        self.sprite.x += self.direction_x * self.velocity_x * self.window.width * delta_time