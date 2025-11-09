from PPlay import sprite
from entity import Entity
from main import UP, LEFT, RIGHT, DOWN

class Player(Entity):
    walking_vel_x = 0.3 # ~320 px em 1080p
    jump_start_vel = 0.37  # 400 px em 1080p
    # is_jumping = False
    
    def __init__(self, window, level, gravity):
        super().__init__(window, level, gravity)
        self.velocity_x = self.walking_vel_x
    
    def setup_sprite(self, assets_path, left_sprite_image, right_sprite_image):
        self.left_sprite = sprite.Sprite(f"assets/{assets_path}{left_sprite_image}.png")
        self.right_sprite = sprite.Sprite(f"assets/{assets_path}{right_sprite_image}.png")
        if self.direction_x != LEFT:
            self.sprite = self.right_sprite
        else:
            self.sprite = self.left_sprite

    
    def set_direction_x(self, direction_x):
        #erro de pulando pro teto ta aqui
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
        if direction_y != self.direction_y:
            self.direction_y = direction_y
    
    def move(self, delta_time):
        if self.direction_x is not None:
            self.velocity_x = self.direction_x * self.walking_vel_x
        else:
            self.velocity_x = 0
        self.sprite.x += self.velocity_x * delta_time * self.window.width
        
        #self.is_on_horizontal_limit(self.direction_x)
        
        if self.is_on_vertical_limit(DOWN):
            print("on floor")
            if self.direction_y == UP:
               self.velocity_y = -self.jump_start_vel
        else:
            print("not on floor")
            self.velocity_y += self.gravity * delta_time
            self.sprite.y += self.velocity_y * delta_time * self.window.height
            if self.is_on_vertical_limit(DOWN):
                self.sprite.y = self.level.floor_y - self.sprite.height * self.window.height
                self.velocity_y = 0