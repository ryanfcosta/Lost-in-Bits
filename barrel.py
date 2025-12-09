from bullet import Bullet

class Barrel(Bullet):
    def __init__(self, window, level, x, y):
        pos_x_norm = x / window.width
        
        super().__init__(window, level, "level_4/", "barrel", pos_x_norm, 0)

        self.sprite.x = x
        self.sprite.y = y
        self.velocity_y = 300 
        self.alive = True

    def move(self, delta_time):
        if not self.alive: return
        self.sprite.y += self.velocity_y * delta_time
        if self.sprite.y > self.window.height:
            self.alive = False
            self.sprite.y = -1000 