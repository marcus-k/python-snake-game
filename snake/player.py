from pygame import image
from enum import Enum
from pathlib import Path

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Player:
    body_asset = image.load(Path(__file__).parent / "assets/snake_body.png")
    x = []          # Body x locations
    y = []          # Body y locations
    speed = 100     # Speed in pixels
    length = 0      # Body length
    
    def __init__(self, length) -> None:
        """
        Initialize the snake body.
        """
        self.body_asset = self.body_asset.convert()
        self.length = length
        for i in range(length):
            self.x.append(0)
            self.y.append(0)

    def move(self, dir: Direction) -> None:
        """
        Move the snake body accordingly with specified direction.
        """
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if dir is Direction.UP:
            self.y[0] -= self.speed
        elif dir is Direction.DOWN:
            self.y[0] += self.speed
        elif dir is Direction.LEFT:
            self.x[0] -= self.speed
        elif dir is Direction.RIGHT:
            self.x[0] += self.speed

    def draw(self, screen) -> None:
        """
        Draw the snake body on the screen.
        """
        for i in range(self.length):
            screen.blit(self.body_asset, (self.x[i], self.y[i]))