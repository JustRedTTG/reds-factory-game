import os
import pygameextra as pe
from atexit import register as atexit
from engine.Save import Save
import engine.Config as cnfg

pe.init((0, 0))
cnfg.config = cnfg.Config()
config = cnfg.config
atexit(config.save)

if os.path.isfile(cnfg.save_location):
    config.load()
else:
    config.save()

config.current_save = Save()
for x in range(50):
    for y in range(50):
        config.current_save.chunks[x, y].compute()
        print(x, y)

print(config.current_save.chunks[1, 1])