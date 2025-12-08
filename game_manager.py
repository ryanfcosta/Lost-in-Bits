from PPlay import window, sprite
import player
from constants import UP, LEFT, RIGHT, DOWN, GRAVITY
import main_menu

class Game:
    menu = "main_menu"
    up_move_key = "W"
    left_move_key = "A"
    right_move_key = "D"

    def __init__(self, window):
        self.window = window
        self.keyboard = window.get_keyboard()
        self.level = None
        self.main_menu = main_menu.MainMenu(window, "menu/", self)
    
    def setup_level(self):
        self.level.load_level()
        
        self.level.player = player.Player(self.window, self.level, "", "josh_left", "josh_right")
        
        self.level.player.sprite.x = self.window.width / 10
        self.level.player.sprite.y = self.level.floor_y - self.level.player.sprite.height
    
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
        if self.menu == "main_menu":
            self.main_menu.load_menu()
        elif self.menu == "game":
            self.level_loop()
        
        self.window.update()
    
    def level_loop(self):
        delta_time = self.window.delta_time()
        
        player_input_direction_x = self.get_player_input_direction_x(self.keyboard)
        self.level.player.set_direction_x(player_input_direction_x)
        
        player_input_direction_y = self.get_player_input_direction_y(self.keyboard)
        self.level.player.set_direction_y(player_input_direction_y)

        self.level.player.move(delta_time)
        
        self.level.background.draw()
        self.level.player.sprite.draw()
        
        for npc in self.level.npcs:
            if npc.alive:
                npc.move(delta_time)
                npc.sprite.x += self.level.background.x
                npc.sprite.draw()
                npc.sprite.x -= self.level.background.x
        
        self.window.draw_text(self.level.level_name, self.window.width - 350, 20, size=30, color=(0, 0, 0), font_name="Arial", bold=True)
        self.level.handle_player_collisions()
    
    # yet to be done
    def has_game_saved(self):
        return False