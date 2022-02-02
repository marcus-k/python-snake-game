from pygame import image
from pathlib import Path

class Apple:
    body_asset = image.load(Path(__file__).parent / "assets/apple.png")
    x = 0
    y = 0

    def __init__(self, x, y, block_size) -> None:
        self.body_asset = self.body_asset.convert()
        
        self.block_size = block_size
        self.x = x * self.block_size
        self.y = y * self.block_size
        

    def draw(self, screen) -> None:
        """
        Draw the apple on the screen.
        """
        screen.blit(self.body_asset, (self.x, self.y))