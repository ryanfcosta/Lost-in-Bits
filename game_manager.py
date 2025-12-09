from PPlay import window, sprite, gameimage, sound
import player
from constants import UP, LEFT, RIGHT, DOWN, GRAVITY, STATES_PER_SECOND, REWIND_DURATION_SECS, FREEZE_DURATION_SECS
import main_menu, characters_menu

TIME_PER_SAVE = 1.0 / STATES_PER_SECOND
TIME_PER_STATE = 1.0 / (STATES_PER_SECOND * 2)

class Game:
    menu = "main_menu"
    up_move_key = "W"
    left_move_key = "A"
    right_move_key = "D"
    char_name = "josh"

    def __init__(self, window):
        self.window = window
        self.keyboard = window.get_keyboard()
        self.mouse = window.get_mouse()
        self.level = None
        self.main_menu = main_menu.MainMenu(window, "menu/", self)
        self.characters_menu = characters_menu.CharactersMenu(window, "menu/", self)
        self.mouse_current_state = None
        self.mouse_previous_state = None

        self.death_sound = sound.Sound("assets/death_sound.mp3")

        self.rewind_ability_box = gameimage.GameImage("assets/rewind_ability_box.png")
        self.rewind_ability_box.x = self.window.width * 0.025
        self.rewind_ability_box.y = self.window.height * 0.025
        self.freeze_ability_box = gameimage.GameImage("assets/freeze_ability_box.png")
        self.freeze_ability_box.x = self.rewind_ability_box.x + self.rewind_ability_box.width + 40
        self.freeze_ability_box.y = self.rewind_ability_box.y
        
        self.collected_cartridges = 0
        self.collected_coolers = 0
        
        self.rewinding_sound = sound.Sound("assets/rewind_sound.mp3")
        self.is_rewinding = False
        self.current_rewind_states = 0
        self.save_state_counter = 0.0
        self.rewind_state_counter = 0.0

        self.freezing_sound = sound.Sound("assets/freeze_sound.mp3")
        self.is_freezing = False
        self.freeze_state_counter = 0.0
        self.freezing_effect = sprite.Sprite("assets/freezing_effect.png")
    
    def reload_player(self):
        self.level.player.setup_sprite("", f"{self.char_name}_left", f"{self.char_name}_right")
    
    def setup_level(self):
        self.level.load_level()
        
        self.level.player = player.Player(self.window, self.level, "", f"{self.char_name}_left", f"{self.char_name}_right")
        
        if hasattr(self.level, 'set_player_start_position'):
            self.level.set_player_start_position()
        else:
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
        self.mouse_current_state = self.mouse.is_button_pressed(1)
        mouse_clicked = self.mouse_current_state and not self.mouse_previous_state
        if self.menu == "main_menu":
            self.main_menu.load_menu(self.mouse, mouse_clicked)
        elif self.menu == "characters_menu":
            self.characters_menu.load_menu(self.mouse, mouse_clicked)
        elif self.menu == "game":
            self.level_loop()
        
        self.window.update()
        self.mouse_previous_state = self.mouse_current_state
    
    def level_loop(self):
        delta_time = self.window.delta_time()

        # Drawing logic
        self.level.background.draw()
        self.level.player.sprite.draw()
        
        for npc in self.level.npcs:
            if npc.alive:
                npc.sprite.x += self.level.background.x
                npc.sprite.draw()
                npc.sprite.x -= self.level.background.x
        for platform in self.level.platforms:
            platform.draw()
        
        self.level.door.draw()
        
        self.rewind_ability_box.draw()
        self.freeze_ability_box.draw()
        self.window.draw_text("Rewind - X", self.rewind_ability_box.x + 45, self.rewind_ability_box.y + 18, size=30, color=(255, 255, 255), font_name="Comic Sans MS")
        self.window.draw_text(f"{(self.collected_cartridges / 4):.0%}", self.rewind_ability_box.x + 85, self.rewind_ability_box.y + 53, size=30, color=(255, 255, 255), font_name="Comic Sans MS")
        self.window.draw_text("Congelar - C", self.freeze_ability_box.x + 35, self.freeze_ability_box.y + 18, size=30, color=(255, 255, 255), font_name="Comic Sans MS")
        self.window.draw_text(f"{(self.collected_coolers / 4):.0%}", self.freeze_ability_box.x + 85, self.freeze_ability_box.y + 53, size=30, color=(255, 255, 255), font_name="Comic Sans MS")
        self.window.draw_text(self.level.level_name, self.window.width - 350, 20, size=30, color=self.level.title_color, font_name="Comic Sans MS", bold=True)

        if self.is_freezing:
            self.freezing_effect.draw()
            self.freezing_step(delta_time)
        
        if self.is_rewinding:
            self.rewind_step(delta_time)
            return

        if self.keyboard.key_pressed("RETURN"):
            self.collected_cartridges += 1
            self.collected_coolers += 1
            self.freezing_sound = sound.Sound("assets/freeze_za_warudo_sound.mp3")
        
        if self.keyboard.key_pressed("X") and self.collected_cartridges >= 4 and not self.is_freezing:
            self.start_rewind_ability()
        
        if self.keyboard.key_pressed("C") and self.collected_coolers >= 4 and not self.is_rewinding and not self.is_freezing:
            self.start_freezing_ability()
        
        self.save_states(delta_time)
        
        player_input_direction_x = self.get_player_input_direction_x(self.keyboard)
        self.level.player.set_direction_x(player_input_direction_x)
        player_input_direction_y = self.get_player_input_direction_y(self.keyboard)
        self.level.player.set_direction_y(player_input_direction_y)
        
        self.level.player.move(delta_time)
        if not self.is_freezing:
            for npc in self.level.npcs:
                if npc.alive:
                    npc.move(delta_time) 
            self.level.handle_player_collisions()
    
    def save_states(self, delta_time):
        self.save_state_counter += delta_time

        if self.save_state_counter >= TIME_PER_SAVE:
            while self.save_state_counter >= TIME_PER_SAVE:
                self.level.save_state(self.level.background.x)
                self.level.player.save_state()
                for npc in self.level.npcs:
                    npc.save_state()
                for platform in self.level.platforms:
                    platform.save_state()
                
                self.save_state_counter -= TIME_PER_SAVE
    
    def start_freezing_ability(self):
        self.is_freezing = True
        self.collected_coolers -= 4
        self.freezing_sound.play()
    
    def freezing_step(self, delta_time):
        self.freeze_state_counter += delta_time
        if self.freeze_state_counter >= FREEZE_DURATION_SECS:
            self.is_freezing = False
            self.freeze_state_counter = 0.0
    
    def start_rewind_ability(self):
        self.is_rewinding = True
        self.current_rewind_states = len(self.level.player.states)
        self.collected_cartridges -= 4
        self.rewinding_sound.play()
    
    def rewind_step(self, delta_time):
        if self.current_rewind_states <= 0:
            self.current_rewind_states = 0
            self.rewind_state_counter = 0.0
            self.is_rewinding = False
            return
        
        self.rewind_state_counter += delta_time

        if self.rewind_state_counter >= TIME_PER_STATE:
            while self.rewind_state_counter >= TIME_PER_STATE:
                if self.current_rewind_states <= 0:
                    self.rewind_state_counter = 0.0
                    break

                if self.level.player.states:
                    state = self.level.player.states.pop()
                    self.level.player.load_state(state)
                
                if self.level.states:
                    state = self.level.states.pop()
                    self.level.background.x = state.background_x

                    if hasattr(state, "door_x"):
                        self.level.door.x = state.door_x
                
                for platform in self.level.platforms:
                    if platform.states:
                        state = platform.states.pop()
                        platform.load_state(state)
                
                for npc in self.level.npcs:
                    if npc.states:
                        state = npc.states.pop()
                        npc.load_state(state)
                
                self.current_rewind_states -= 1
                self.rewind_state_counter -= TIME_PER_STATE
        
        if self.current_rewind_states <= 0:
            self.is_rewinding = False
    
    # yet to be done
    def has_game_saved(self):
        return False
