import pygame
from pygame.locals import *
from pathlib import Path
import time
from random import randint

from .player import Player, Direction
from .apple import Apple

class Game:
    window_size = (400, 400)
    block_size = 10
    game_over = False

    def __init__(self, verbose=False) -> None:
        self.verbose = verbose

        # Initialize PyGame settings and display
        pygame.init()
        self._screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_icon(
            pygame.image.load(Path(__file__).parent / "assets/apple.png")
        )
        pygame.display.set_caption("Snake Game")
        self._running = True

        # Add snake to the game
        self.player = Player(4, self.block_size)

        # Add apple to the game, not on top of the snake
        x, y = self.player.x, self.player.y
        while x == self.player.x and y == self.player.y:
            x = randint(0, self.window_size[0] / self.block_size - 1)
            y = randint(0, self.window_size[1] / self.block_size - 1)
            if verbose:
                print(f"apple: {x * self.block_size}, {y * self.block_size}")

        self.apple = Apple(x, y, self.block_size)
    
    def render(self) -> None:
        self._screen.fill(Color("black"))   # Background color
        self.player.draw(self._screen)      # Draw snake
        self.apple.draw(self._screen)       # Draw apple

        pygame.display.update()             # Update current display

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
                self.player.dir = Direction.RIGHT
            if keys[K_a]:
                self.player.dir = Direction.LEFT
            if keys[K_s]:
                self.player.dir = Direction.DOWN
            if keys[K_w]:
                self.player.dir = Direction.UP

            self.player.move()
    
            if self.verbose and any(keys):
                print(f"Player: ({self.player.x}, {self.player.y})")

            self.check_apple()
            self.check_snake()

            if self.game_over:
                break

            # Render new positions
            self.render()
            time.sleep(200 / 1000)

        pygame.quit()

    def check_apple(self) -> None:
        """
        Check if the apple has been eaten by the snake.
        """
        if self.player.x[0] == self.apple.x:
            if self.player.y[0] == self.apple.y:
                self.player.eat()
                self.apple.respawn(self.window_size)

    def check_snake(self) -> None:
        """
        Check if the snake has gone out of bounds or eaten itself
        """
        # Out of bounds
        if not 0 <= self.player.x[0] < self.window_size[0]:
            self.game_over = True
        elif not 0 <= self.player.y[0] < self.window_size[1]:
            self.game_over = True
        
        # Eaten itself
        elif self.player.x[0] in self.player.x[1:]:
            if self.player.y[0] in self.player.y[1:]:
                self.game_over = True
        