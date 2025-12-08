from PPlay import window
import game_manager, plumber_level, pacman_level,scaled_window

window = scaled_window.ScaledWindow(1920, 1080)

if __name__ == "__main__":
    game = game_manager.Game(window)
    pacman_level = pacman_level.PacmanLevel(game, "level_2/", None)
    plumber_level = plumber_level.PlumberLevel.create_level_instance(game, "level_1/", "background")
    #game.level = pacman_level
    game.level = plumber_level
    game.setup_level()

    while True:
        game.game_loop()