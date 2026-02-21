import numpy as np
import scipy

import constants

class Crust:
    def __init__(self, model):
        self.model = model

        self.map = self.model.rng.integers(
            low=constants.INITIAL_PLANET_CRUST_MIN,
            high=constants.INITIAL_PLANET_CRUST_MAX,
            size=self.model.size()
        )

        self.map = scipy.ndimage.gaussian_filter(self.map, .9)
