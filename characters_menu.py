from PPlay import sprite

class CharactersMenu:
    def __init__(self, window, assets_path, game):
        self.window = window
        self.assets_path = assets_path
        self.game = game

        self.josh_display = self.setup_sprite("josh_display")
        self.lua_display = self.setup_sprite("lua_display")
        self.bbot_display = self.setup_sprite("bbot_display")

        self.josh_display.x = window.width / 4 - self.josh_display.width / 2
        self.lua_display.x = window.width * 2 / 4 - self.lua_display.width / 2
        self.bbot_display.x = window.width * 3 / 4 - self.bbot_display.width / 2

        self.josh_display.y = window.height / 2 - self.josh_display.height / 2
        self.lua_display.y = window.height / 2 - self.lua_display.height / 2
        self.bbot_display.y = window.height / 2 - self.bbot_display.height / 2
        
        self.josh_btn = self.setup_sprite("josh")
        self.lua_btn = self.setup_sprite("lua")
        self.bbot_btn = self.setup_sprite("bbot")
        
        btn_width = self.josh_btn.width
        btn_height = self.josh_btn.height

        josh_btn_x = window.width / 4 - btn_width / 2
        lua_btn_x = window.width * 2 / 4 - btn_width / 2
        bbot_btn_x = window.width * 3 / 4 - btn_width / 2
        btn_y = window.height * 3 / 4 - btn_height / 2

        self.josh_btn.set_position(josh_btn_x, btn_y)
        self.lua_btn.set_position(lua_btn_x, btn_y)
        self.bbot_btn.set_position(bbot_btn_x, btn_y)
    
    def load_menu(self, mouse, mouse_clicked):
        self.window.set_background_color([100, 200, 255])
        self.josh_display.draw()
        self.lua_display.draw()
        self.bbot_display.draw()

        self.josh_btn.draw()
        self.lua_btn.draw()
        self.bbot_btn.draw()

        if mouse_clicked:
            if mouse.is_over_object(self.josh_btn):
                self.game.char_name = "josh"
            elif mouse.is_over_object(self.lua_btn):
                self.game.char_name = "lua"
            elif mouse.is_over_object(self.bbot_btn):
                self.game.char_name = "bbot"
            else:
                return
            self.game.reload_player()
            self.game.menu = "main_menu"
    
    def setup_sprite(self, asset):
        return sprite.Sprite(f"assets/{self.assets_path}{asset}.png")