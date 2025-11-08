from abstract_level import AbstractLevel

class PlumberLevel(AbstractLevel):
    floor_relative_height = 0.8
    level_name = "Plumber Level"
    
    def __init__(self, window, assets_path, background_image):
        super().__init__(window, assets_path, background_image, PlumberLevel.floor_relative_height)