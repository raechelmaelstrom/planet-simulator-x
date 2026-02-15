import logging
import sys

import pygame

import planetmodel
import planetvisualizer

LOG = logging.getLogger("main")

def main():
    pygame.init()

    pm = planetmodel.PlanetModel()
    pv = planetvisualizer.PlanetVisualizer(pm)
    pv.run()

    pygame.quit()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    LOG.info("Starting up!")
    main()
    sys.exit(0)
