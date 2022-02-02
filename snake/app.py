import pygame
from pygame.locals import *
import time

from .player import Player, Direction

class App:
    window_size = (500, 500)

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Snake Game")
        self._running = True

        self.player = Player(4)
    
    def render(self) -> None:
        self._screen.fill(Color("black"))   # Background color
        self.player.draw(self._screen)      # Draw snake

        pygame.display.update()

    def run(self) -> None:
        """
        Main event loop.
        """
        while self._running:
            # Check for the window closing
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False

            # Check which direction is pressed
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
            time.sleep(100 / 1000)

        pygame.quit()