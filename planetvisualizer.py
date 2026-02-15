import logging

import pygame

import constants

LOG = logging.getLogger("PlanetVisualizer")

class PlanetVisualizer:

    def __init__(self, model):
        pygame.display.set_caption("Planet Simulator X")
        self.screen = pygame.display.set_mode((constants.RESOLUTION_WIDTH, constants.RESOLUTION_HEIGHT))
        self.clock = pygame.time.Clock()
        LOG.info("Screen initialized")

        self.model = model
        self.paused = False
        self.cursor_x = 0
        self.cursor_y = 0

    def _event_handler(self) -> bool:
        # Handles all keyboard and input events.
        # Returns True if we should keep running,
        # False if we should quit.

        # Lock display to max FPS of 60
        self.clock.tick(constants.MAX_FPS)
        fps = self.clock.get_fps() 
        LOG.debug(f"FPS: {fps}")
        LOG.debug(f"Cursor: {self.cursor_x}, {self.cursor_y}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            # Pause
            self.paused = not self.paused
        if keys[pygame.K_w]:
            # Up
            self.cursor_y -= 1
        if keys[pygame.K_s]:
            # Down
            self.cursor_y += 1
        if keys[pygame.K_a]:
            # Left
            self.cursor_x -= 1
        if keys[pygame.K_d]:
            # Right
            self.cursor_x += 1


        return True

    def run(self):
        tile_size = 32

        y_tiles = int(constants.RESOLUTION_HEIGHT / tile_size) + 1
        x_tiles = int(constants.RESOLUTION_WIDTH / tile_size) + 1

        # Game loop
        while self._event_handler():
            if self.paused:
                continue

            LOG.debug("Drawing screen...")
            self.screen.fill((0,0,0))

            y = 0
            while y <= y_tiles:

                x = 0
                while x <= x_tiles:
                    x_pos = x * tile_size
                    y_pos = y * tile_size

                    #LOG.debug(f"Drawing tile ({x}, {y}) at ({x_pos}, {y_pos})")

                    pygame.draw.rect(
                            self.screen, 
                            (0, 0, self.model.world[self.cursor_x + x][self.cursor_y + y]),
                            (x_pos, y_pos, tile_size, tile_size)
                    )

                    x += 1
                y += 1

            pygame.display.flip()

