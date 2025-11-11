from PPlay import window
import game_manager, plumber_level, scaled_window

window = scaled_window.ScaledWindow(1920, 1080)

if __name__ == "__main__":
    game = game_manager.Game(window)
    plumber_level = plumber_level.PlumberLevel(window, "level_1/", "background")
    game.level = plumber_level
    game.setup_level()

    while True:
        game.game_loop()