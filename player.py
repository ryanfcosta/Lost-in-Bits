from PPlay import sprite
from entity import Entity
from constants import UP, LEFT, RIGHT, DOWN, GRAVITY

class Player(Entity):
    walking_vel_x = 0.2
    jump_start_vel = 0.6
    
    def __init__(self, window, level, assets_path, left_sprite_image, right_sprite_image):
        super().__init__(window, level)
        self.velocity_x = self.walking_vel_x
        self.setup_sprite(assets_path, left_sprite_image, right_sprite_image)
    
    def setup_sprite(self, assets_path, left_sprite_image, right_sprite_image):
        self.left_sprite = sprite.Sprite(f"assets/{assets_path}{left_sprite_image}.png")
        self.right_sprite = sprite.Sprite(f"assets/{assets_path}{right_sprite_image}.png")
        if self.direction_x != LEFT:
            self.sprite = self.right_sprite
        else:
            self.sprite = self.left_sprite

    
    def set_direction_x(self, direction_x):
        self.direction_x = direction_x
        if direction_x is None or (self.sprite == self.left_sprite and direction_x == LEFT) or (self.sprite == self.right_sprite and direction_x == RIGHT):
            return
        if direction_x == LEFT:
            new_sprite = self.left_sprite
        else:
            new_sprite = self.right_sprite
        new_sprite.x = self.sprite.x
        new_sprite.y = self.sprite.y
        self.sprite = new_sprite
    
    def set_direction_y(self, direction_y):
        if not self.is_on_vertical_limit(DOWN): # tá no ar
            self.direction_y = DOWN
        elif direction_y != self.direction_y:
            self.direction_y = direction_y
    
    def move(self, delta_time):
        if (self.direction_x == LEFT and not self.is_on_horizontal_limit(LEFT)) or (self.direction_x == RIGHT and not self.is_on_horizontal_limit(RIGHT)):
            self.velocity_x = self.direction_x * self.walking_vel_x
        else:
            self.velocity_x = 0
        self.move_x(self.velocity_x * self.window.width * delta_time)
        
        if self.is_on_vertical_limit(DOWN):
            if self.direction_y == UP:
                self.velocity_y = -self.jump_start_vel
            else:
                self.sprite.y = self.level.floor_y - self.sprite.height
                self.direction_y = None
                self.velocity_y = 0
        else: # tá no ar
            if self.direction_y == DOWN:  
                self.velocity_y += GRAVITY * self.direction_y * delta_time
        self.sprite.y += self.velocity_y * self.window.height * delta_time

    def move_x(self, x_change):
        background = self.level.background
        if x_change > 0: # indo pra direita
            player_on_left_half = (self.sprite.x - (self.sprite.width / 2)) <= (self.window.width / 2)
            background_right_limit_reached = (background.x + background.width) <= self.window.width
            if player_on_left_half or background_right_limit_reached:
                self.sprite.x += x_change
            else:
                background.x -= x_change
        else: # indo pra esquerda
            player_on_right_half = (self.sprite.x + (self.sprite.width / 2)) >= (self.window.width / 2)
            background_left_limit_reached = background.x >= 0
            if player_on_right_half or background_left_limit_reached:
                self.sprite.x += x_change
            else:
                background.x -= x_change
