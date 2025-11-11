from PPlay import window, sprite
import player
from main import UP, LEFT, RIGHT, DOWN

class Game:
    up_move_key = "W"
    left_move_key = "A"
    right_move_key = "D"
    
    gravity = 1.5

    def __init__(self, window):
        self.window = window
        self.keyboard = window.get_keyboard()
        self.current_level = None
    
    def setup_level(self):
        self.current_level.load_level()
        
        self.player = player.Player(self.window, self.current_level, self.gravity)
        self.player.setup_sprite("", "josh_left", "josh_right")
        
        self.player.sprite.x = self.window.width / 10
        self.player.sprite.y = self.current_level.floor_y - self.player.sprite.height
    
    def get_player_input_direction_x(self, keyboard):
        if keyboard.key_pressed(self.left_move_key) and not keyboard.key_pressed(self.right_move_key):
            return LEFT
        if keyboard.key_pressed(self.right_move_key) and not keyboard.key_pressed(self.left_move_key):
            return RIGHT
        return None
    
    def get_player_input_direction_y(self, keyboard):
        if keyboard.key_pressed(self.up_move_key):
            return UP
        return None
    
    def game_loop(self):
        delta_time = self.window.delta_time()
        
        player_input_direction_x = self.get_player_input_direction_x(self.keyboard)
        self.player.set_direction_x(player_input_direction_x)
        
        player_input_direction_y = self.get_player_input_direction_y(self.keyboard)
        self.player.set_direction_y(player_input_direction_y)

        self.player.move(delta_time)
        
        self.current_level.background.draw()
        self.player.sprite.draw()
        self.window.draw_text(self.current_level.level_name, self.window.width - 350, 20, size=30, color=(0, 0, 0), font_name="Arial", bold=True)
        self.window.update()