import pygame
from pygame.locals import *
from pathlib import Path
import time

from .player import Player, Direction
from .apple import Apple

class Game:
    window_size = (800, 800)
    block_size = 10

    def __init__(self, verbose=False) -> None:
        self.verbose = verbose

        pygame.init()
        self._screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_icon(
            pygame.image.load(Path(__file__).parent / "assets/apple.png")
        )
        pygame.display.set_caption("Snake Game")
        self._running = True

        self.player = Player(4, self.block_size)
        self.apple = Apple(10, 10, self.block_size)
    
    def render(self) -> None:
        self._screen.fill(Color("black"))   # Background color
        self.player.draw(self._screen)      # Draw snake
        self.apple.draw(self._screen)       # Draw apple

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
            if self.verbose and any(keys):
                print(f"Player: ({self.player.x}, {self.player.y})")

            # Check for if apple is eaten (move inside player.move(dir, self))
            if self.collision(self.player.x[0], self.player.y[0], self.apple.x, self.apple.y):
                self.player.eat()
                self.apple.respawn(self.window_size)


            self.render()
            time.sleep(200 / 1000)

        pygame.quit()

    def collision(self, x1, y1, x2, y2) -> bool:
        """
        Check for collision between two cells.
        """
        return x1 == x2 and y1 == y2