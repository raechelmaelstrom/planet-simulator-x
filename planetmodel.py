import numpy as np

import constants

class PlanetModel:
    def __init__(self):
        self.rng = np.random.default_rng()
        size = (constants.PLANET_TILES_X, constants.PLANET_TILES_Y)
        self.world = self.rng.integers(low=0, high=255, size=size)

