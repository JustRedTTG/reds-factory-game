import random

from pygameextra.infinitygrid import Grid, GridObject
import engine.Config as cnfg
from numpy import cos, sin, pi, array

chunk_size = 10
config = lambda: cnfg.config

z1 = pi / 180.
z2 = 1 / 360

def shift(v: float):
    rnd = 1/random.randint(1, 10)
    return min(1, max(0.1, v-rnd))


def maxgrid(v: float):
    return min(0, max(chunk_size-1, int(v)))


def calc(position, radius, am_p: (int, float) = 1):
    cos360 = list(cos(array([i / am_p for i in range(0, int(360 * am_p + 1))]) * z1))
    sin360 = list(sin(array([i / am_p for i in range(0, int(360 * am_p + 1))]) * z1))
    return [(maxgrid(position[0] + shift(c) * radius), maxgrid(position[1] - shift(s) * radius)) for c, s in zip(cos360, sin360)]

def get_chunk_seed(x, y):
    return config().current_save.get_noise(x, y)


class Chunk:
    def __init__(self):
        self.grid = Grid(chunk_size, chunk_size)

    def generate(self, seed):
        if seed == 0: return
        wc = self.grid.width // 2 # center width
        hc = self.grid.height // 2 # center height
        points = calc((wc, hc), chunk_size // 2, 1/30) # 12
        print(points)




class BlankChunk(GridObject):
    def compute(self = None):
        BlankChunk.grid[BlankChunk.x, BlankChunk.y] = Chunk()
        BlankChunk.grid[BlankChunk.x, BlankChunk.y].generate(get_chunk_seed(BlankChunk.x, BlankChunk.y))
        return BlankChunk.grid[BlankChunk.x, BlankChunk.y] or self