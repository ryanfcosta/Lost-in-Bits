from PPlay import sprite

class Platform:
    def __init__(self, window, level):
        self.window = window
        self.level = level
    
    def set_platform(self, x,y, n, assets_path, sprite_image):
        print("AJSDOAODJAPASSEI AQUI")
        self.blocks = [None] * n
        for i in range(n):
            self.blocks[i] = sprite.Sprite(f"assets/{assets_path}{sprite_image}.png")
            self.blocks[i].y = y
            self.blocks[i].x = x if i == 0 else x + (self.blocks[i].width * i)

    def draw(self):
            for block in self.blocks:
                block.draw()
    
    # pra plataforma mover com a camera
    def move_x(self, x_change):
        for block in self.blocks:
            block.x += x_change