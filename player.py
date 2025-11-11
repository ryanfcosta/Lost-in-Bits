from PPlay import sprite
from entity import Entity
from constants import UP, LEFT, RIGHT, DOWN, GRAVITY

class Player(Entity):
    walking_vel_x = 0.2
    jump_start_vel = 0.6
    
    def __init__(self, window, level, assets_path, left_sprite_image, right_sprite_image):
        super().__init__(window, level)
        self.setup_sprite(assets_path, left_sprite_image, right_sprite_image)
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_on_floor = False #flag pra checar o chao e plat
        self.direction_y = DOWN #gravidade funfar no inicio
    
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
    
    # func pra pular da plataforma e chao
    def set_direction_y(self, direction_y): 
        if direction_y == UP and self.is_on_floor:
            self.direction_y = UP
    
    def move(self, delta_time):
        #x
        if (self.direction_x == LEFT) or (self.direction_x == RIGHT):
            self.velocity_x = self.direction_x * self.walking_vel_x
        else:
            self.velocity_x = 0
        x_change = self.velocity_x * self.window.width * delta_time

        #colisao lateral
        self.sprite.x += x_change
        for platform in self.level.platforms:
            for block in platform.blocks:
                if self.sprite.collided(block):
                    if x_change > 0: #indo p direita
                        self.sprite.x = block.x - self.sprite.width
                    elif x_change < 0: #voltando
                        self.sprite.x = block.x + block.width
                    break 
        
        #y
        if self.direction_y == UP and self.is_on_floor: 
            self.velocity_y = -self.jump_start_vel
            self.is_on_floor = False
        self.direction_y = DOWN #reseta pulo
        
        #grav
        if not self.is_on_floor:
            self.velocity_y += GRAVITY * DOWN * delta_time
            if self.velocity_y > GRAVITY * 2:
                 self.velocity_y = GRAVITY * 2
        y_change = self.velocity_y * self.window.height * delta_time
        self.sprite.y += y_change
        self.is_on_floor = False #reset flag

        #colis chão
        if self.is_on_vertical_limit(DOWN):
            self.sprite.y = self.level.floor_y - self.sprite.height 
            self.velocity_y = 0      
            self.is_on_floor = True 

        #colisão com plat
        for platform in self.level.platforms:
            for block in platform.blocks:
                if self.sprite.collided(block):
                    if y_change > 0: #caiu
                        self.sprite.y = block.y - self.sprite.height 
                        self.velocity_y = 0
                        self.is_on_floor = True
                    elif y_change < 0: #bate cabeça
                        self.sprite.y = block.y + block.height
                        self.velocity_y = 0
        self.move_x(x_change)#chama camera dps de testar col

    def move_x(self, x_change):
        background = self.level.background

        if x_change > 0: 
            player_on_left_half = (self.sprite.x - (self.sprite.width / 2)) <= (self.window.width / 2)
            background_right_limit_reached = (background.x + background.width) <= self.window.width
            if player_on_left_half or background_right_limit_reached:
                if (self.sprite.x + self.sprite.width) > self.window.width:
                    self.sprite.x = self.window.width - self.sprite.width
            else:
                background.x -= x_change
                self.sprite.x -= x_change
                for platform in self.level.platforms: #anda c x de cada plat
                    platform.move_x(-x_change) 

        elif x_change < 0:
            player_on_right_half = (self.sprite.x + (self.sprite.width / 2)) >= (self.window.width / 2)
            background_left_limit_reached = background.x >= 0
            if player_on_right_half or background_left_limit_reached:
                if self.sprite.x < 0:
                    self.sprite.x = 0
            else:
                background.x -= x_change
                self.sprite.x -= x_change
                for platform in self.level.platforms: #anda c x de cada plat
                    platform.move_x(-x_change)