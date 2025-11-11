import pygame
from PPlay.window import Window
from PPlay import keyboard, mouse

class ScaledWindow(Window):    
    def __init__(self, width, height):
        # Input controllers
        Window.keyboard = keyboard.Keyboard()
        Window.mouse = mouse.Mouse()
        
        # Size
        self.width = width
        self.height = height

        # Pattern color
        self.color = [0,0,0]  # Black

        # Pattern Title
        self.title = "Title"

        # Time Control
        self.curr_time = 0  # current frame time
        self.last_time = 0  # last frame time 
        self.total_time = 0  # += curr-last(delta_time), update()

        # Creates the screen (pygame.Surface)
        # There are some useful flags (look pygame's docs)
        # It's like a static attribute in Java
        #Window.screen = pygame.display.set_mode([self.width, self.height])
        Window.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN | pygame.SCALED)
        # ? Why is it possible to do w.screen?

        # Sets pattern starting conditions
        self.set_background_color(self.color)
        self.set_title(self.title)

        # Updates the entire screen if no arguments are passed
        # Can be used to update portions of the screen (Rect list)
        pygame.display.update()