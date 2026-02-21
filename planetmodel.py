import logging

import numpy as np
import scipy

import constants
import crust
import meteor

LOG = logging.getLogger("PlanetModel")

class PlanetModel:
    def __init__(self):
        self.rng = np.random.default_rng()

        self.crust = crust.Crust(self)

    def meteor_impact(self, coords):
        m = meteor.Meteor(self, coords)
        m.calculate_impact()

    def size(self):
        return (constants.PLANET_TILES_X, constants.PLANET_TILES_Y)
