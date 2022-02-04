from pygame import image
from pathlib import Path

class RestartButton:
    body_asset = image.load(Path(__file__).parent / "assets/restart.png")
    x: int  # Top left x coordinate of button
    y: int  # Top left y coordinate of button

    def __init__(self, x, y) -> None:
        self.body_asset = self.body_asset.convert()
        self.x = x
        self.y = y

    def draw(self, screen):
        """
        Draw the button on the screen.
        """
        return screen.blit(self.body_asset, (self.x, self.y))
