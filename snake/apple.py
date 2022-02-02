from pygame import image
from pathlib import Path

class Apple:
    body_asset = image.load(Path(__file__).parent / "assets/apple.png")
    x = 0
    y = 0
    block_size = 10

    def __init__(self, x, y) -> None:
        self.x = x * self.block_size
        self.y = y * self.block_size
        self.body_asset = self.body_asset.convert()

    def draw(self, screen) -> None:
        """
        Draw the apple on the screen.
        """
        screen.blit(self.body_asset, (self.x, self.y))