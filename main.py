from PPlay import window
import pygame
import game_manager, plumber_level

window = window.Window(1920, 1080)

pygame.init()
pygame.display.set_mode((window.width, window.height), pygame.FULLSCREEN)

game = game_manager.Game(window)
plumber_level = plumber_level.PlumberLevel(window, "level_1/", "background")
game.current_level = plumber_level
game.setup_level()

while True:
    game.game_loop()