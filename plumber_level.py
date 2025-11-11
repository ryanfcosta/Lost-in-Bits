from abstract_level import AbstractLevel
import game_platform

class PlumberLevel(AbstractLevel):
    floor_relative_height = 0.8
    level_name = "Plumber Level"
    sprite_name = "floor_brick"
    level_path = "level_1/"
    #floor brick 60x60


    def __init__(self, window, assets_path, background_image):
        super().__init__(window, assets_path, background_image, PlumberLevel.floor_relative_height)

        self.platforms = []

        platform_1 = game_platform.Platform(self.window, self)
        platform_1.set_platform(700,740,3,"level_1/", "floor_brick")
        self.platforms.append(platform_1)
       
        platform_2 = game_platform.Platform(self.window, self)
        platform_2.set_platform(1000, 630, 8, "level_1/", "floor_brick")
        self.platforms.append(platform_2)

        platform_3 = game_platform.Platform(self.window, self)
        platform_3.set_platform(1400, 570, 2, "level_1/", "floor_brick")
        self.platforms.append(platform_3)

        platform_4 = game_platform.Platform(self.window, self)
        platform_4.set_platform(1600, 720, 4, "level_1/", "floor_brick")
        self.platforms.append(platform_4)

        platform_5 = game_platform.Platform(self.window, self)
        platform_5.set_platform(2000, 715, 10, "level_1/", "floor_brick")
        self.platforms.append(platform_5)

        platform_6 = game_platform.Platform(self.window, self)
        platform_6.set_platform(2800, 680, 2, "level_1/", "floor_brick")
        self.platforms.append(platform_6)

        platform_7 = game_platform.Platform(self.window, self)
        platform_7.set_platform(3000, 630, 2, "level_1/", "floor_brick")
        self.platforms.append(platform_7)

        platform_8 = game_platform.Platform(self.window, self)
        platform_8.set_platform(3300, 550, 6, "level_1/", "floor_brick")
        self.platforms.append(platform_8)

        platform_9 = game_platform.Platform(self.window, self)
        platform_9.set_platform(3800, 700, 12, "level_1/", "floor_brick")
        self.platforms.append(platform_9)

        platform_10 = game_platform.Platform(self.window, self)
        platform_10.set_platform(4500, 670, 1, "level_1/", "floor_brick")
        self.platforms.append(platform_10)

        platform_11 = game_platform.Platform(self.window, self)
        platform_11.set_platform(4650, 668, 1, "level_1/", "floor_brick")
        self.platforms.append(platform_11)

        platform_12 = game_platform.Platform(self.window, self)
        platform_12.set_platform(4800, 665, 1, "level_1/", "floor_brick")
        self.platforms.append(platform_12)

        platform_13 = game_platform.Platform(self.window, self)
        platform_13.set_platform(5000, 660, 7, "level_1/", "floor_brick")
        self.platforms.append(platform_13)

        platform_14 = game_platform.Platform(self.window, self)
        platform_14.set_platform(5400, 740, 4, "level_1/", "floor_brick")
        self.platforms.append(platform_14)