import config
import pyxel


class Package:
    """
    Class for a package in the game.

    Attributes:
        level : int
            The conveyor level of the package (starts at 0, ends at 6).
        state : str
            The state of the package. "in_conveyor", "handled", "broken",
            "at_truck", "other".
    """

    def __init__(self, state: str = "in_conveyor"):
        # Attributes
        self.level = 0              # initial level set to 0
        self.tick = 0
        self.x = config.WIDTH - 1.5*config.TILE_DIMENSION - self.tick*config.TILE_DIMENSION
        self.y = config.HEIGHT - 2*config.TILE_DIMENSION - 4 - self.level*config.TILE_DIMENSION
        self.state = state

        # Methods
        self.draw()

    # level property
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if not isinstance(level, int):
            raise TypeError("level must be an integer")
        elif level < 0 or level > 6:
            raise ValueError("level must be beetwen 0 and 6")
        self.__level = level

    # state property
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        if not isinstance(state, str):
            raise TypeError("state must be a string")
        elif state not in config.PACKAGE_STATES:
            raise ValueError(f"state must be one of: {config.PACKAGE_STATES}")
        self.__state = state

    def update(self):
        """
        update method for package class
        """

    def draw(self):
        if self.state == "CONVEYOR":
            sprite = config.PACKAGE_SPRITE[self.level]
        elif self.state == "HANDLED":
            sprite = (2, 0, 0, 8, 8, 0)  # Empty sprite
        elif self.state == "BROKEN":
            sprite = config.PACKAGE_SPRITE[self.level]
        else:
            sprite = (2, 0, 0, 8, 8, 0)  # Empty sprite

        pyxel.blt(self.x, self.y, *sprite)
