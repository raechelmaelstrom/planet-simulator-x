import logging

import pygame

import constants

LOG = logging.getLogger("PlanetVisualizer")

class PlanetVisualizer:

    def __init__(self, model):
        self.model = model

        pygame.display.set_caption("Planet Simulator X")
        self.screen = pygame.display.set_mode((constants.RESOLUTION_WIDTH, constants.RESOLUTION_HEIGHT))
        self.clock = pygame.time.Clock()
        LOG.info("Screen initialized")

        self.paused = False

        # Top x,y coordinates in model of viewing window
        self.window_x = 0
        self.window_y = 0

        self.tile_size = 32
        self.y_tiles = int(constants.RESOLUTION_HEIGHT / self.tile_size) + 1
        self.x_tiles = int(constants.RESOLUTION_WIDTH / self.tile_size) + 1

    def _map_tile_to_model(self, tile_x, tile_y) -> tuple[int, int]:
        # Map from tile-space to coordinates in the model
        size_x, size_y = self.model.size()
        model_x = self.window_x + tile_x
        if model_x >= size_x:
            model_x -= size_x

        model_y = self.window_y + tile_y
        if model_y >= size_y:
            model_y -= size_y

        return (model_x, model_y)

    def _event_handler(self) -> bool:
        # Handles all keyboard and input events.
        # Returns True if we should keep running,
        # False if we should quit.

        # Lock display to max FPS of 60
        self.clock.tick(constants.MAX_FPS)
        fps = self.clock.get_fps() 
        LOG.debug(f"FPS: {fps}")
        LOG.debug(f"Window: {self.window_x}, {self.window_y}")

        model_size_x, model_size_y = self.model.size()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            # Pause
            self.paused = not self.paused
        if keys[pygame.K_w]:
            # Up
            if self.window_y > 0:
                self.window_y -= 1
        if keys[pygame.K_s]:
            # Down
            if self.window_y + self.y_tiles < model_size_y:
                self.window_y += 1
        if keys[pygame.K_a]:
            # Left
            self.window_x -= 1

            # If we've scrolled left over the edge...
            if self.window_x < 0:
                self.window_x += model_size_x
                LOG.debug("Wrapping left: %d", self.window_x)

        if keys[pygame.K_d]:
            # Right
            self.window_x += 1

            # If we've scrolled right over the edge...
            if self.window_x >= model_size_x:
                self.window_x -= model_size_x

        return True

    def run(self):
        while self._event_handler():
            if self.paused:
                continue

            LOG.debug("Drawing screen...")
            self.screen.fill((0,0,0))

            y = 0
            while y <= self.y_tiles:

                x = 0
                while x <= self.x_tiles:
                    x_pos = x * self.tile_size
                    y_pos = y * self.tile_size

                    model_x, model_y = self._map_tile_to_model(x, y)
                    #LOG.debug("Drawing tile %s at %s with model data %s",
                    #          (x, y), (x_pos, y_pos), (model_x, model_y))

                    pygame.draw.rect(
                            self.screen, 
                            (0, 0, self.model.world[model_x][model_y]),
                            (x_pos, y_pos, self.tile_size, self.tile_size)
                    )

                    x += 1
                y += 1

            pygame.display.flip()

