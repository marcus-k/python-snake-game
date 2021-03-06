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
    tail_x = 0              # Previous tail x location
    tail_y = 0              # Previous tail y location
    dir = Direction.DOWN    # Current facing direction
    
    def __init__(self, length: int, block_size: int) -> None:
        """
        Initialize the snake body.
        """
        self.body_asset = self.body_asset.convert()

        self.length = length            # Snake length
        self.block_size = block_size    # Grid block size
        self.x = []                     # Body x locations
        self.y = []                     # Body y locations
        for i in range(length):
            self.x.append(5 * block_size)
            self.y.append(5 * block_size)

    def move(self, dir: Direction = None) -> None:
        """
        Move the snake body accordingly with specified direction.
        """
        if dir is None:
            dir = self.dir

        # Current snake head location
        current_x = self.x[0]
        current_y = self.y[0]

        # Move head forwards
        if dir is Direction.UP:
            self.x.insert(0, current_x)
            self.y.insert(0, current_y - self.block_size)
        elif dir is Direction.DOWN:
            self.x.insert(0, current_x)
            self.y.insert(0, current_y + self.block_size)
        elif dir is Direction.LEFT:
            self.x.insert(0, current_x - self.block_size)
            self.y.insert(0, current_y)
        elif dir is Direction.RIGHT:
            self.x.insert(0, current_x + self.block_size)
            self.y.insert(0, current_y)

        # Store old tail position
        self.tail_x = self.x.pop()
        self.tail_y = self.y.pop()

    def eat(self) -> None:
        """
        Add length to snake, restore tail position.
        """
        self.length += 1
        self.x.append(self.tail_x)
        self.y.append(self.tail_y)

    def draw(self, screen) -> None:
        """
        Draw the snake body on the screen.
        """
        for i in range(self.length):
            screen.blit(self.body_asset, (self.x[i], self.y[i]))
