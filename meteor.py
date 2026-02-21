import logging
import math

import constants

LOG = logging.getLogger("Meteor")

class Meteor:
    def __init__(self, model, coords):
        self.coords = coords
        self.model = model

    def calculate_impact(self):
        x, y = self.coords

        LOG.info(f"Got hit by a meteor at ({x}, {y})")

        # Depth of transient crater from asteroid impact
        # https://impact.ese.ic.ac.uk/ImpactEarth/ImpactEffects/effects.pdf

        # Density of the target area on the planet being impacted in kg/m^3
        planet_density = 2700

        # Density of the asteroid in kg/m^3
        asteroid_density = 2750

        # Asteroid diameter after atmospheric entry in m
        asteroid_diameter = 18000

        # Asteroid impact velocity at surface in m/s
        asteroid_velocity = 20000

        # Angle of impact measured in degrees to horizontal
        impact_angle = 45 # degrees

        # Planet surface gravity in m/s^2
        planet_gravity = constants.PLANET_GRAVITY

        # Diameter of the transient crater in m (eq. 21*)
        d_tc = 1.161 * \
            pow((asteroid_density / planet_density), 1/3) * \
            pow(asteroid_diameter, 0.78) * \
            pow(asteroid_velocity, 0.44) * \
            pow(planet_gravity, -0.22) * \
            pow(math.sin(math.radians(impact_angle)), 1/3)

        # If it's a large (complex) crater (>3200 meters):
        if d_tc > 3200:
            # Eq 27
            final_diameter_km = 1.17 * pow(d_tc / 1000, 1.13) / pow(3.2, 0.13)
            final_diameter = final_diameter_km * 1000
        else:
            # Final diameter of crater in m (eq. 22)
            final_diameter = d_tc * 1.25

        rim_height = 0.07 * pow(d_tc, 4) / pow(final_diameter, 3)

        # Eq 28 (in m)
        final_depth = 0.4 * pow((final_diameter / 1000), .3) * 1000

        LOG.info("Crater diameter of %d, rim height %d, depth %d", final_diameter, rim_height, final_depth)

        # TODO: make size of crater correct
        # Decrease altitude of impact
        self.model.crust.map[x-1][y-1] += rim_height
        self.model.crust.map[x-1][y] += rim_height
        self.model.crust.map[x-1][y+1] += rim_height
        self.model.crust.map[x+1][y-1] += rim_height
        self.model.crust.map[x+1][y] += rim_height
        self.model.crust.map[x+1][y+1] += rim_height
        self.model.crust.map[x][y+1] += rim_height
        self.model.crust.map[x][y-1] += rim_height

        self.model.crust.map[x][y] -= final_depth 
