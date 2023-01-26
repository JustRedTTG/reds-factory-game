import random
from pygameextra.infinitygrid import Inf_grid, GridObject
from engine.Chunk import Chunk, BlankChunk
from perlin_noise import PerlinNoise
from math import floor

class Noise(GridObject):
    def get(self, x, y):
        x = x-1000*self.x
        y = y-1000*self.y
        noise_val = self.value[0]([x / 1000, y / 1000])
        noise_val += self.value[1]([x / 1000, y / 1000])
        noise_val += self.value[2]([x / 1000, y / 1000])
        noise_val += self.value[3]([x / 1000, y / 1000])
        return round(noise_val)

class BlankNoise(Noise):
    po1: int
    po2: int
    po3: int
    po4: int
    seed: int
    def get(*args, **kwargs):
        BlankNoise.grid[BlankNoise.x, BlankNoise.y] = Noise(
            [
                PerlinNoise(octaves=BlankNoise.po1, seed=BlankNoise.seed),
                PerlinNoise(octaves=BlankNoise.po2, seed=BlankNoise.seed),
                PerlinNoise(octaves=BlankNoise.po3, seed=BlankNoise.seed),
                PerlinNoise(octaves=BlankNoise.po4, seed=BlankNoise.seed)
            ],
            BlankNoise.grid,
            BlankNoise.x,
            BlankNoise.y
        )
        return BlankNoise.grid[BlankNoise.x, BlankNoise.y].get(*args, **kwargs)


class Save:
    seed: int = None
    chunks: Inf_grid = None
    camera_position: tuple = None

    def __init__(self, seed: int = None,
                 po1: int = 48,
                 po2: int = 96,
                 po3: int = 192,
                 po4: int = 384):
        BlankNoise.po1, BlankNoise.po2, BlankNoise.po3, BlankNoise.po4 = po1, po2, po3, po4
        self.seed = seed or random.randint(0, 999_999_999)
        BlankNoise.seed = self.seed
        self.noise_grid = Inf_grid(BlankNoise)
        self.chunks = Inf_grid(BlankChunk)
        self.camera_position = (0, 0)

    def get_noise(self, x, y):
        return self.noise_grid[floor(x/1000), floor(x/1000)].get(x, y)

    def __copy__(self):
        new = Save(self.seed)

        return new