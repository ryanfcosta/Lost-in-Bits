from PPlay import sprite
from constants import STATES_PER_SECOND, REWIND_DURATION_SECS
from collections import deque

class Platform:
    def __init__(self, window, level):
        self.window = window
        self.level = level
        total_states = STATES_PER_SECOND * REWIND_DURATION_SECS
        self.states = deque(maxlen=total_states)
    
    def set_platform(self, x,y, n, assets_path, sprite_image):
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
    
    def load_state(self, state):
        for i, block_state in enumerate(state.block_positions):
            self.blocks[i].x = block_state["x"]
            self.blocks[i].y = block_state["y"]
            
    def save_state(self):
        state = _PlatformState(self.blocks)
        self.states.append(state)


class _PlatformState:
     def __init__(self, blocks):
        self.block_positions = []
        for block in blocks:
            self.block_positions.append({
                "x": block.x,
                "y": block.y
            })