from PPlay import sprite

class MainMenu:
    def __init__(self, window, assets_path, game):
        self.window = window
        self.assets_path = assets_path
        self.game = game
        self.new_game_btn = self.setup_button_sprite("new_game")
        self.options_btn = self.setup_button_sprite("character")
        self.quit_btn = self.setup_button_sprite("quit")
        btn_width = self.new_game_btn.width
        btn_x = (self.window.width - btn_width) // 2
        btn_height = self.new_game_btn.height
        total_buttons_height = 3 * btn_height
        gap = (self.window.height - total_buttons_height) // 4
        top = gap
        self.new_game_btn.set_position(btn_x, top)
        self.options_btn.set_position(btn_x, top + btn_height + gap)
        self.quit_btn.set_position(btn_x, top + 2 * (btn_height + gap))
    
    def load_menu(self, mouse, mouse_clicked):
        self.window.set_background_color([92, 64, 51])
        self.new_game_btn.draw()
        self.options_btn.draw()
        self.quit_btn.draw()

        if mouse_clicked:
            if mouse.is_over_object(self.new_game_btn):
                self.game.menu = "game"
            elif mouse.is_over_object(self.options_btn):
                self.game.menu = "characters_menu"
            elif mouse.is_over_object(self.quit_btn):
                exit()
    
    def setup_button_sprite(self, asset):
        assets_path = self.assets_path
        if assets_path and not assets_path.endswith("/"):
            assets_path = assets_path + "/"
        return sprite.Sprite(f"assets/{assets_path}{asset}.png")