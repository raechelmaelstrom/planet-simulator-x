import numpy as np
import scipy

import constants

class PlanetModel:
    def __init__(self):
        self.rng = np.random.default_rng()
        self.world = self.rng.integers(
            low=constants.INITIAL_PLANET_CRUST_MIN,
            high=constants.INITIAL_PLANET_CRUST_MAX,
            size=self.size()
        )

        self.world = scipy.ndimage.gaussian_filter(self.world, .9)

    def size(self):
        return (constants.PLANET_TILES_X, constants.PLANET_TILES_Y)

