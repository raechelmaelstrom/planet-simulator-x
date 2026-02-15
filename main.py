import logging
import sys

import pygame

import planetvisualizer

LOG = logging.getLogger("main")

def main():
    pygame.init()

    pv = planetvisualizer.PlanetVisualizer()
    pv.run()

    pygame.quit()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    LOG.info("Starting up!")
    main()
    sys.exit(0)
