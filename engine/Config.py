from pygameextra.display import get_size as get_display_size
from hexicapi.save import save, load
from copy import copy

save_location = 'savedata.pickle'

class Config:
    color: tuple[int, int, int]
    padding: float

    saves: list['Save', ...]
    width: int
    height: int
    current_save: 'Save'
    def __init__(self):
        self.color = (235, 235, 235)
        self.padding = .1

        # Temp
        self.saves = []
        self.width, self.height = get_display_size()
        self.zoom = 0.1


    def save(self):
        data = copy(self), *[copy(save) for save in self.saves]
        save(save_location, *data)

    def load(self):
        config, *saves = load(save_location)
        self.color = config.color
        self.padding = config.padding
        self.saves = saves

    def __copy__(self):
        new = Config()
        new.color = self.color
        new.padding = self.padding
        return new

config: Config
