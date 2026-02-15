import logging

import pygame

import constants

LOG = logging.getLogger("PlanetVisualizer")

class PlanetVisualizer:

    def __init__(self):
        pygame.display.set_caption("Planet Simulator X")
        self.screen = pygame.display.set_mode((constants.RESOLUTION_WIDTH, constants.RESOLUTION_HEIGHT))
        self.clock = pygame.time.Clock()
        LOG.info("Screen initialized")

    def _event_handler(self) -> bool:
        # Handles all keyboard and input events.
        # Returns True if we should keep running,
        # False if we should quit.

        # Lock display to max FPS of 60
        self.clock.tick(constants.MAX_FPS)
        fps = self.clock.get_fps() 
        LOG.debug(f"FPS: {fps}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        return True

    def run(self):
        # Define colors (R, G, B)
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)

        # Create a pygame.Rect object
        # Syntax: pygame.Rect(left, top, width, height)
        rect_position_and_size = pygame.Rect(50, 50, 100, 75)

        blue_shade = 0
        tile_size = 32

        # Game loop
        while self._event_handler():
            LOG.debug("Drawing screen...")
            self.screen.fill(BLACK)

            y = 0
            while y < constants.RESOLUTION_HEIGHT:

                x = 0
                while x < constants.RESOLUTION_WIDTH:
                    #LOG.debug(f"Drawing tile ({x}, {y}) with color {blue_shade}")

                    pygame.draw.rect(
                            self.screen, 
                            (0, 0, blue_shade), 
                            (x, y, tile_size, tile_size)
                    )

                    blue_shade += 1
                    if blue_shade > 255:
                        blue_shade = 0

                    x += tile_size

                y += tile_size


            pygame.display.flip()

