from pygame import image
from enum import Enum
from pathlib import Path

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Player:
    x = 10
    y = 10
    speed = 1
    body_asset = image.load(Path(__file__).parent / "assets/snake_body.png")
    
    def __init__(self) -> None:
        self.body_asset = self.body_asset.convert()

    def move(self, dir: Direction) -> None:
        if dir is Direction.UP:
            self.y -= self.speed
        elif dir is Direction.DOWN:
            self.y += self.speed
        elif dir is Direction.LEFT:
            self.x -= self.speed
        elif dir is Direction.RIGHT:
            self.x += self.speed