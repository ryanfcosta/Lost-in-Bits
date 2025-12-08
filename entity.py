from PPlay import sprite
from constants import UP, LEFT, RIGHT, DOWN, STATES_PER_SECOND, REWIND_DURATION_SECS
from collections import deque

class Entity:    
    def __init__(self, window, level):
        self.window = window
        self.level = level
        self.velocity_x = None
        self.velocity_y = None
        self.direction_x = None
        self.direction_y = None
        self.x_left_limit = 0
        self.x_right_limit = 1
        self.alive = True
        
        total_states = STATES_PER_SECOND * REWIND_DURATION_SECS
        self.states = deque(maxlen=total_states)
    
    def setup_sprite(self, assets_path, sprite_image):
        self.sprite = sprite.Sprite(f"assets/{assets_path}{sprite_image}.png")
    
    def move(self, delta_time):
        pass
    
    def is_on_horizontal_limit(self, direction):
        if direction == LEFT:
            return self.sprite.x <= (self.x_left_limit * self.window.width)
        elif direction == RIGHT:
            return (self.sprite.x + self.sprite.width) >= (self.x_right_limit * self.window.width)
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
    
    def load_state(self, state):
        self.sprite.x = state.x
        self.sprite.y = state.y
        self.direction_x = state.direction_x
        self.direction_y = state.direction_y
        self.velocity_x = state.velocity_x
        self.velocity_y = state.velocity_y
        self.alive = state.alive
    
    def save_state(self):
        state = _EntityState(
            self.sprite.x,
            self.sprite.y,
            self.direction_x,
            self.direction_y,
            self.velocity_x,
            self.velocity_y,
            self.alive
        )

        self.states.append(state)

class _EntityState:
    def __init__(self, x, y, direction_x, direction_y, velocity_x, velocity_y, alive):
        self.x = x
        self.y = y
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.alive = alive