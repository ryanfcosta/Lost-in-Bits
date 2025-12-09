from PPlay import sprite
from collections import deque
from constants import STATES_PER_SECOND, REWIND_DURATION_SECS

class AbstractLevel:
    def __init__(self, game, assets_path, background_image, floor_relative_height):
        self.game = game
        self.window = game.window
        self.assets_path = assets_path
        self.background_image = background_image
        self.background = sprite.Sprite(f"assets/{assets_path}{background_image}.png")        
        self.floor_y = game.window.height * floor_relative_height
        self.door = None

        total_states = STATES_PER_SECOND * REWIND_DURATION_SECS
        self.states = deque(maxlen=total_states)
    
    def load_level(self):
        self.npcs = []
    
    def save_state(self, background_x):
        door_x = self.door.x if self.door is not None else None
        state = _LevelState(background_x, door_x)
        self.states.append(state)

class _LevelState:
    def __init__(self, background_x, door_x):
        self.background_x = background_x
        self.door_x = door_x