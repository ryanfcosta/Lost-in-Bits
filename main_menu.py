from PPlay import sprite

class MainMenu:
    def __init__(self, window, assets_path, game):
        self.window = window
        self.assets_path = assets_path
        self.new_game_btn = self.setup_button_sprite("new_game")
        if game.has_game_saved():
            self.continue_btn = self.setup_button_sprite("continue")
        else:
            self.continue_btn = self.setup_button_sprite("continue_disabled")
        self.options_btn = self.setup_button_sprite("options")
        self.quit_btn = self.setup_button_sprite("quit")
        
        btn_width = self.new_game_btn.width
        btn_x = (window.width - btn_width) / 2
        btn_height = self.new_game_btn.height
        btn_spacing = (window.height - 4 * btn_height) / 5
        
        self.new_game_btn.set_position(btn_x, btn_spacing)
        self.continue_btn.set_position(btn_x, 2 * btn_spacing + btn_height)
        self.options_btn.set_position(btn_x, 3 * btn_spacing + 2 * btn_height)
        self.quit_btn.set_position(btn_x, 4 * btn_spacing + 3 * btn_height)
    
    def load_menu(self):
        self.window.set_background_color([255, 255, 255])
        self.new_game_btn.draw()
        self.continue_btn.draw()
        self.options_btn.draw()
        self.quit_btn.draw()
    
    def setup_button_sprite(self, asset):
        return sprite.Sprite(f"assets/{self.assets_path}{asset}.png")