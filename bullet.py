from entity import Entity

class Bullet(Entity):
    walking_vel_x = 0.05

    def __init__(self, window, level, assets_path, sprite_image, pos_x, direction_x):
        super().__init__(window, level)
        self.velocity_x = self.walking_vel_x
        self.direction_x = direction_x
        self.alive = True
        self.setup_sprite(assets_path, sprite_image)
        #limite pela direita é 0
        self.x_limit = window.width
        self.sprite.x = pos_x * window.width
        self.sprite.y = level.floor_y - self.sprite.height 
    
    def move(self, delta_time):
        self.sprite.x += self.direction_x * self.velocity_x * self.window.width * delta_time