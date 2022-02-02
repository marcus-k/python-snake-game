import pygame
from pygame.locals import *

from .player import Player, Direction

class App:
    window_size = (800, 600)

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Snake Game")
        self._running = True

        self.player = Player()
    
    def render(self):
        self._screen.fill(Color("black"))
        self._screen.blit(self.player.body_asset, (self.player.x, self.player.y))

        pygame.display.update()

    def run(self) -> None:
        """Main event loop."""
        while self._running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False

            keys = pygame.key.get_pressed()
            if keys[K_d]:
                self.player.move(Direction.RIGHT)
            if keys[K_a]:
                self.player.move(Direction.LEFT)
            if keys[K_s]:
                self.player.move(Direction.DOWN)
            if keys[K_w]:
                self.player.move(Direction.UP)

            self.render()

        pygame.quit()